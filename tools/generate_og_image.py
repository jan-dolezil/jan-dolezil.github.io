#!/usr/bin/env python3
"""Generate the Open Graph / Twitter share image (og-image.jpg, 1200x630).

Local-only helper: lives in tools/ so it is versioned in git but NEVER
published to GitHub Pages (deploy workflow copies an explicit allow-list
of files into _site/, and tools/ is not on it).

Tinkerables: COLORS / FONTS / LINES below.

Usage:
    pip install Pillow
    python3 tools/generate_og_image.py            # writes into repo root
    python3 tools/generate_og_image.py --out tmp  # preview elsewhere
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# --- Tinker zone -----------------------------------------------------------
W, H = 1200, 630
NAVY = (0, 0, 128)
YELLOW = (255, 255, 0)
GRAY = (192, 192, 192)
WHITE = (255, 255, 255)
BODY = (40, 40, 40)
LINK = (0, 0, 180)

FONTS = {
    "eyebrow": ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 34),
    "name": ("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 110),
    "sub": ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 44),
    "body": ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 36),
    "url": ("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 36),
}
LINES = [
    # (y, text, font_key, color)
    (120, "\u2605  JAN DOLE\u017dIL  \u2605", "eyebrow", NAVY),
    (200, "Jan Dole\u017eil", "name", NAVY),
    (350, "Cybernetics & Robotics \u2014 CTU Prague", "sub", NAVY),
    (430, "Computer Vision ", "body", BODY),
    (510, "jan-dolezil.github.io", "url", LINK),
]
OUT_NAME = "og-image.jpg"
REPO_ROOT = Path(__file__).resolve().parent.parent
# ---------------------------------------------------------------------------


def load_font(key: str) -> ImageFont.FreeTypeFont:
    path, size = FONTS[key]
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()


def center(draw: ImageDraw.ImageDraw, y: int, text: str, font, fill) -> None:
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw) / 2 - bbox[0], y), text, font=font, fill=fill)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default=str(REPO_ROOT), help="output directory")
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    # outer yellow border, then inner gray panel echoing the retro theme
    d.rectangle([0, 0, W - 1, H - 1], outline=YELLOW, width=10)
    d.rectangle([60, 60, W - 60, H - 60], fill=GRAY, outline=WHITE, width=6)

    fonts = {k: load_font(k) for k in FONTS}
    for y, text, key, color in LINES:
        center(d, y, text, fonts[key], color)

    target = out / OUT_NAME
    img.save(target, "JPEG", quality=88, optimize=True, progressive=True)
    print(f"wrote {target} ({W}x{H}, {target.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
