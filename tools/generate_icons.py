#!/usr/bin/env python3
"""Generate favicons + PWA icons for jan-dolezil.github.io.

Local-only helper: lives in tools/ so it is versioned in git but NEVER
published to GitHub Pages (deploy workflow copies an explicit allow-list
of files into _site/, and tools/ is not on it).

Tinkerables: NAVY / YELLOW / TEXT / FONT_PATH / SIZES below.

Usage:
    pip install Pillow
    python3 tools/generate_icons.py            # writes into repo root
    python3 tools/generate_icons.py --out tmp  # preview elsewhere

Outputs (repo root):
    favicon-16x16.png, favicon-32x32.png,
    apple-touch-icon.png (180x180),
    icon-192.png, icon-512.png,
    favicon.ico (multi-size 16/32/48, built from icon-512.png)
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# --- Tinker zone -----------------------------------------------------------
NAVY = (0, 0, 128)        # page navy (#000080)
YELLOW = (255, 255, 0)    # retro yellow (#ff0)
TEXT = "JD"
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
# output filename -> pixel size
SIZES = {
    "favicon-16x16.png": 16,
    "favicon-32x32.png": 32,
    "apple-touch-icon.png": 180,
    "icon-192.png": 192,
    "icon-512.png": 512,
}
REPO_ROOT = Path(__file__).resolve().parent.parent
# ---------------------------------------------------------------------------


def load_font(size_px: int):
    try:
        return ImageFont.truetype(FONT_PATH, size_px)
    except Exception:
        return ImageFont.load_default()


def draw_icon(size: int) -> Image.Image:
    img = Image.new("RGB", (size, size), NAVY)
    d = ImageDraw.Draw(img)
    # subtle inset border like the retro theme (skip at tiny sizes)
    if size >= 48:
        b = max(1, size // 60)
        d.rectangle([b, b, size - 1 - b, size - 1 - b], outline=YELLOW, width=b)
    font = load_font(int(size * (0.52 if size >= 48 else 0.62)))
    bbox = d.textbbox((0, 0), TEXT, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text(
        ((size - tw) / 2 - bbox[0], (size - th) / 2 - bbox[1] - size * 0.02),
        TEXT,
        font=font,
        fill=YELLOW,
    )
    return img


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default=str(REPO_ROOT), help="output directory")
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    for fname, size in SIZES.items():
        draw_icon(size).save(out / fname)
        print(f"wrote {out / fname} ({size}x{size})")

    # Multi-size ICO rebuilt from the 512 master for crispness.
    master = draw_icon(512)
    master.save(out / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    print(f"wrote {out / 'favicon.ico'} (16/32/48)")


if __name__ == "__main__":
    main()
