"""Генерация синтетической ЭКГ и сохранение полосок demo_25.svg и demo_50.svg."""

from __future__ import annotations

import math
from pathlib import Path
from typing import List

from ekg import render_ekg_svg

# Компоненты одного кардиоцикла: (смещение от R, с; амплитуда, мВ; ширина sigma, с).
# Амплитуды и длительности выбраны близко к нормальной ЭКГ во II отведении.
_WAVES = (
    (-0.16, 0.15, 0.025),   # P
    (-0.025, -0.10, 0.008),  # Q
    (0.0, 1.00, 0.009),      # R
    (0.025, -0.25, 0.008),   # S
    (0.22, 0.30, 0.040),     # T
)


def synthetic_ecg(
    duration_s: float = 10.0,
    sample_rate_hz: float = 500.0,
    heart_rate_bpm: float = 60.0,
    first_beat_s: float = 0.5,
) -> List[float]:
    """Синтетический сигнал ЭКГ (мВ): сумма гауссовых волн P-Q-R-S-T для каждого удара.

    R-зубцы располагаются в моменты ``first_beat_s + k * 60 / heart_rate_bpm``.
    """
    n = int(round(duration_s * sample_rate_hz))
    rr_s = 60.0 / heart_rate_bpm
    beats = []
    t_beat = first_beat_s
    while t_beat < duration_s + 0.5:  # +0.5 с, чтобы T-волна последнего удара не обрывалась
        beats.append(t_beat)
        t_beat += rr_s

    out: List[float] = []
    for i in range(n):
        t = i / sample_rate_hz
        v = 0.0
        for tb in beats:
            for dt, amp, sigma in _WAVES:
                x = (t - tb - dt) / sigma
                if abs(x) < 6.0:
                    v += amp * math.exp(-0.5 * x * x)
        out.append(v)
    return out


def main(out_dir: Path | None = None) -> None:
    out_dir = out_dir or Path(__file__).resolve().parent
    fs = 500.0
    signal = synthetic_ecg(duration_s=10.0, sample_rate_hz=fs, heart_rate_bpm=60.0)
    for speed in (25.0, 50.0):
        svg = render_ekg_svg(signal, fs, speed_mm_s=speed, gain_mm_mv=10.0)
        path = out_dir / f"demo_{int(speed)}.svg"
        path.write_text(svg, encoding="utf-8")
        print(f"saved {path}")


if __name__ == "__main__":
    main()
