"""Тесты для ekg.py: геометрия полоски в миллиметрах."""

from __future__ import annotations

import re
from typing import List, Tuple

import pytest

from demo import synthetic_ecg
from ekg import (
    DEFAULT_GAIN_MM_MV,
    EkgLayout,
    parse_signal_points,
    render_ekg_svg,
    signal_to_points,
)

FS = 500.0
HR_BPM = 60.0
RR_S = 60.0 / HR_BPM


def _r_peaks(points: List[Tuple[float, float]], baseline_mm: float, gain_mm_mv: float):
    """Локальные максимумы амплитуды выше 0.5 мВ (R-зубцы); возвращает их x в мм.

    В SVG ось Y направлена вниз, поэтому амплитуда = (baseline - y) / gain.
    """
    amp = [(baseline_mm - y) / gain_mm_mv for _, y in points]
    threshold = 0.5
    peaks = []
    for i in range(1, len(amp) - 1):
        if amp[i] > threshold and amp[i] >= amp[i - 1] and amp[i] > amp[i + 1]:
            peaks.append(points[i][0])
    return peaks


@pytest.fixture(scope="module")
def signal():
    return synthetic_ecg(duration_s=10.0, sample_rate_hz=FS, heart_rate_bpm=HR_BPM)


def _attr(svg: str, name: str) -> float:
    m = re.search(rf'{name}="([^"]+)"', svg)
    assert m, f"attribute {name} not found"
    return float(m.group(1))


def test_rr_distance_at_25_mm_s(signal):
    """При 25 мм/с и RR = 1 с расстояние между R-зубцами в SVG равно 25 мм."""
    svg = render_ekg_svg(signal, FS, speed_mm_s=25.0, gain_mm_mv=DEFAULT_GAIN_MM_MV)
    pts = parse_signal_points(svg)
    baseline = _attr(svg, "data-baseline-mm")
    peaks = _r_peaks(pts, baseline, DEFAULT_GAIN_MM_MV)

    assert len(peaks) == 10  # 10 с при 60/мин, первый удар на 0.5 с
    expected_mm = RR_S * 25.0  # 25 мм
    for a, b in zip(peaks, peaks[1:]):
        # допуск — один отсчёт (25 мм/с / 500 Гц = 0.05 мм) + округление до 0.001 мм
        assert b - a == pytest.approx(expected_mm, abs=25.0 / FS + 1e-3)


def test_rr_distance_doubles_at_50_mm_s(signal):
    """При 50 мм/с те же R-зубцы отстоят друг от друга на 50 мм."""
    svg = render_ekg_svg(signal, FS, speed_mm_s=50.0)
    pts = parse_signal_points(svg)
    peaks = _r_peaks(pts, _attr(svg, "data-baseline-mm"), DEFAULT_GAIN_MM_MV)
    assert len(peaks) == 10
    for a, b in zip(peaks, peaks[1:]):
        assert b - a == pytest.approx(RR_S * 50.0, abs=50.0 / FS + 1e-3)


def test_r_amplitude_matches_gain(signal):
    """R-зубец амплитудой 1 мВ при 10 мм/мВ возвышается над изолинией на 10 мм."""
    svg = render_ekg_svg(signal, FS, speed_mm_s=25.0, gain_mm_mv=10.0)
    pts = parse_signal_points(svg)
    baseline = _attr(svg, "data-baseline-mm")
    top = min(y for _, y in pts)
    assert baseline - top == pytest.approx(10.0, abs=0.05)


def test_calibration_pulse_is_1mv_and_200ms():
    """Калибровочный зубец: высота 1 мВ * усиление, ширина 0.2 с * скорость."""
    svg = render_ekg_svg([0.0] * 100, 100.0, speed_mm_s=25.0, gain_mm_mv=10.0)
    m = re.search(r'<path class="calibration" d="([^"]+)"', svg)
    assert m
    d = m.group(1)
    x_start, y_base = map(float, re.match(r"M([-\d.]+) ([-\d.]+)", d).groups())
    vs = [float(v) for v in re.findall(r"V([-\d.]+)", d)]
    hs = [float(v) for v in re.findall(r"H([-\d.]+)", d)]
    assert y_base - vs[0] == pytest.approx(10.0)          # 1 мВ * 10 мм/мВ
    assert hs[1] - hs[0] == pytest.approx(0.2 * 25.0)     # 0.2 с * 25 мм/с = 5 мм
    assert vs[1] == pytest.approx(y_base)


def test_viewbox_is_in_millimeters():
    svg = render_ekg_svg([0.0] * 251, 250.0, speed_mm_s=25.0)  # ровно 1 с → 25 мм
    width = re.search(r'width="([\d.]+)mm"', svg)
    assert width, "width must be given in mm"
    vb = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
    assert vb
    assert float(vb.group(1)) == pytest.approx(float(width.group(1)))
    layout = EkgLayout()
    x0 = _attr(svg, "data-signal-x0-mm")
    pts = parse_signal_points(svg)
    assert pts[0][0] == pytest.approx(x0)
    assert pts[-1][0] - pts[0][0] == pytest.approx(25.0)
    # сетка начинается с отступа и кратна 5 мм
    grid = re.search(r'<rect class="paper" x="([\d.]+)" y="([\d.]+)" width="([\d.]+)"', svg)
    assert float(grid.group(1)) == layout.margin_mm
    assert float(grid.group(3)) % 5 == 0


def test_signal_to_points_scaling():
    pts = signal_to_points([0.0, 1.0, -0.5], 10.0, speed_mm_s=50.0, gain_mm_mv=10.0,
                           x0_mm=2.0, baseline_mm=20.0)
    assert pts == [(2.0, 20.0), (7.0, 10.0), (12.0, 25.0)]


@pytest.mark.parametrize("speed", [0.0, 30.0, -25.0])
def test_rejects_nonstandard_speed(speed):
    with pytest.raises(ValueError):
        render_ekg_svg([0.0, 0.1], 10.0, speed_mm_s=speed)


def test_rejects_empty_signal():
    with pytest.raises(ValueError):
        render_ekg_svg([], 10.0)
