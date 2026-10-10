"""Отрисовка ЭКГ-полоски в SVG на миллиметровой сетке.

Все геометрические величины внутри SVG заданы в миллиметрах:
``viewBox`` имеет размеры ``width_mm x height_mm``, а атрибуты ``width``/``height``
используют единицу ``mm``, поэтому при печати масштаб 1:1 сохраняется.

Основная функция — :func:`render_ekg_svg`.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable, List, Sequence, Tuple

__all__ = [
    "EkgLayout",
    "SPEEDS_MM_S",
    "DEFAULT_GAIN_MM_MV",
    "signal_to_points",
    "render_ekg_svg",
    "parse_signal_points",
]

#: Допустимые стандартные скорости протяжки ленты, мм/с.
SPEEDS_MM_S = (25.0, 50.0)
#: Стандартное усиление, мм/мВ.
DEFAULT_GAIN_MM_MV = 10.0
#: Длительность калибровочного зубца, с (стандарт: 1 мВ в течение 200 мс).
CALIBRATION_DURATION_S = 0.2


@dataclass(frozen=True)
class EkgLayout:
    """Геометрия полоски (все значения в мм)."""

    margin_mm: float = 5.0          # отступ сетки от краёв
    calibration_gap_mm: float = 5.0  # зазор между калибровочным зубцом и сигналом
    height_mm: float = 40.0          # высота области сигнала (сетки)
    baseline_mm: float | None = None  # положение изолинии; None = по центру сетки

    def baseline(self) -> float:
        if self.baseline_mm is not None:
            return self.baseline_mm
        return self.margin_mm + self.height_mm / 2.0


def _fmt(value: float) -> str:
    """Компактная запись числа в SVG (3 знака после запятой, без хвостовых нулей)."""
    s = f"{value:.3f}"
    s = s.rstrip("0").rstrip(".") if "." in s else s
    return "0" if s in ("-0", "") else s


def signal_to_points(
    values_mv: Sequence[float],
    sample_rate_hz: float,
    speed_mm_s: float = 25.0,
    gain_mm_mv: float = DEFAULT_GAIN_MM_MV,
    x0_mm: float = 0.0,
    baseline_mm: float = 0.0,
) -> List[Tuple[float, float]]:
    """Перевод отсчётов (мВ) в координаты (мм).

    x = x0 + i / fs * speed,  y = baseline - v * gain  (ось Y в SVG направлена вниз).
    """
    if sample_rate_hz <= 0:
        raise ValueError("sample_rate_hz must be positive")
    if speed_mm_s <= 0 or gain_mm_mv <= 0:
        raise ValueError("speed_mm_s and gain_mm_mv must be positive")
    dx = speed_mm_s / sample_rate_hz
    return [
        (x0_mm + i * dx, baseline_mm - float(v) * gain_mm_mv)
        for i, v in enumerate(values_mv)
    ]


def _grid_svg(x: float, y: float, w: float, h: float) -> str:
    """Миллиметровая сетка: тонкие линии через 1 мм, жирные через 5 мм."""
    minor: List[str] = []
    major: List[str] = []
    n_cols = int(round(w))
    n_rows = int(round(h))
    for i in range(n_cols + 1):
        xi = x + i
        (major if i % 5 == 0 else minor).append(
            f"M{_fmt(xi)} {_fmt(y)}V{_fmt(y + h)}"
        )
    for j in range(n_rows + 1):
        yj = y + j
        (major if j % 5 == 0 else minor).append(
            f"M{_fmt(x)} {_fmt(yj)}H{_fmt(x + w)}"
        )
    return (
        f'<rect class="paper" x="{_fmt(x)}" y="{_fmt(y)}" width="{_fmt(w)}" '
        f'height="{_fmt(h)}"/>\n'
        f'<path class="grid-minor" d="{" ".join(minor)}"/>\n'
        f'<path class="grid-major" d="{" ".join(major)}"/>'
    )


def render_ekg_svg(
    values_mv: Iterable[float],
    sample_rate_hz: float,
    speed_mm_s: float = 25.0,
    gain_mm_mv: float = DEFAULT_GAIN_MM_MV,
    *,
    calibration: bool = True,
    layout: EkgLayout | None = None,
    title: str | None = None,
) -> str:
    """Построить SVG-полоску ЭКГ.

    :param values_mv: отсчёты сигнала в милливольтах.
    :param sample_rate_hz: частота дискретизации, Гц.
    :param speed_mm_s: скорость ленты, мм/с (стандартно 25 или 50).
    :param gain_mm_mv: усиление, мм/мВ (стандартно 10).
    :param calibration: рисовать ли калибровочный зубец 1 мВ в начале полоски.
    :param layout: геометрия полоски (отступы, высота, изолиния), мм.
    :param title: подпись в нижнем левом углу; None = автоматическая.
    :return: строка с SVG-документом, координаты которого заданы в мм.
    """
    values = [float(v) for v in values_mv]
    if not values:
        raise ValueError("values_mv must not be empty")
    if speed_mm_s not in SPEEDS_MM_S:
        raise ValueError(
            f"speed_mm_s must be one of {SPEEDS_MM_S}, got {speed_mm_s!r}"
        )
    if gain_mm_mv <= 0:
        raise ValueError("gain_mm_mv must be positive")
    if sample_rate_hz <= 0:
        raise ValueError("sample_rate_hz must be positive")

    lay = layout or EkgLayout()
    baseline = lay.baseline()

    grid_x = lay.margin_mm
    grid_y = lay.margin_mm
    calib_w = CALIBRATION_DURATION_S * speed_mm_s if calibration else 0.0
    signal_x0 = grid_x + (calib_w + lay.calibration_gap_mm if calibration else 0.0)
    signal_w = (len(values) - 1) / sample_rate_hz * speed_mm_s
    grid_w = signal_x0 - grid_x + signal_w
    grid_w = float(5 * -(-grid_w // 5))  # округляем вверх до жирной линии (5 мм)
    grid_h = lay.height_mm
    width = grid_w + 2 * lay.margin_mm
    height = grid_h + 2 * lay.margin_mm

    pts = signal_to_points(
        values, sample_rate_hz, speed_mm_s, gain_mm_mv, signal_x0, baseline
    )
    points_attr = " ".join(f"{_fmt(x)},{_fmt(y)}" for x, y in pts)

    calib_svg = ""
    if calibration:
        top = baseline - 1.0 * gain_mm_mv  # 1 мВ
        d = (
            f"M{_fmt(grid_x)} {_fmt(baseline)}"
            f"H{_fmt(grid_x + 1)}"
            f"V{_fmt(top)}"
            f"H{_fmt(grid_x + 1 + calib_w)}"
            f"V{_fmt(baseline)}"
            f"H{_fmt(signal_x0)}"
        )
        calib_svg = f'<path class="calibration" d="{d}"/>\n'

    label = title if title is not None else (
        f"{_fmt(speed_mm_s)} mm/s   {_fmt(gain_mm_mv)} mm/mV   "
        f"fs = {_fmt(sample_rate_hz)} Hz   "
        f"{_fmt(len(values) / sample_rate_hz)} s"
    )

    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{_fmt(width)}mm" height="{_fmt(height)}mm" '
        f'viewBox="0 0 {_fmt(width)} {_fmt(height)}" '
        f'data-speed-mm-s="{_fmt(speed_mm_s)}" data-gain-mm-mv="{_fmt(gain_mm_mv)}" '
        f'data-sample-rate-hz="{_fmt(sample_rate_hz)}" '
        f'data-baseline-mm="{_fmt(baseline)}" data-signal-x0-mm="{_fmt(signal_x0)}">\n'
        "<style>\n"
        "  .paper { fill: #fff7f5; }\n"
        "  .grid-minor { stroke: #f3b6b6; stroke-width: 0.1; fill: none; }\n"
        "  .grid-major { stroke: #e57373; stroke-width: 0.25; fill: none; }\n"
        "  .calibration { stroke: #111; stroke-width: 0.3; fill: none;\n"
        "                 stroke-linejoin: round; }\n"
        "  .signal { stroke: #111; stroke-width: 0.3; fill: none;\n"
        "            stroke-linejoin: round; stroke-linecap: round; }\n"
        "  .label { font: 2.5px sans-serif; fill: #333; }\n"
        "</style>\n"
        f"{_grid_svg(grid_x, grid_y, grid_w, grid_h)}\n"
        f"{calib_svg}"
        f'<polyline class="signal" points="{points_attr}"/>\n'
        f'<text class="label" x="{_fmt(grid_x)}" y="{_fmt(height - 1.5)}">{label}</text>\n'
        "</svg>\n"
    )


_POLYLINE_RE = re.compile(r'<polyline class="signal" points="([^"]*)"')


def parse_signal_points(svg: str) -> List[Tuple[float, float]]:
    """Извлечь из SVG координаты (мм) точек сигнала — обратная операция для тестов."""
    m = _POLYLINE_RE.search(svg)
    if not m:
        raise ValueError("no signal polyline found in SVG")
    pts: List[Tuple[float, float]] = []
    for token in m.group(1).split():
        xs, ys = token.split(",")
        pts.append((float(xs), float(ys)))
    return pts
