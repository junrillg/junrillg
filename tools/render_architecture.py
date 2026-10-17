#!/usr/bin/env python3
"""Render the conceptual architecture artwork with Pillow (no network needed)."""

import argparse
import math
from pathlib import Path

WIDTH, HEIGHT, SCALE = 1200, 440, 2
FRAMES, DURATION = 80, 70
GROUND = (9, 10, 27)
INK = (246, 245, 253)
ACCENT = (185, 163, 251)


def arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "assets",
                        help="destination directory (default: repository assets/)")
    parser.add_argument("--font", type=Path, help="optional TrueType/OpenType font; defaults to an installed sans-serif")
    return parser.parse_args()


def font_path(requested):
    if requested:
        if not requested.is_file():
            raise FileNotFoundError(requested)
        return requested
    candidates = [
        Path("/System/Library/Fonts/Supplemental/Arial.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        Path("C:/Windows/Fonts/arial.ttf"),
    ]
    return next((p for p in candidates if p.is_file()), None)


def projection(point, phase):
    x, y, z = point
    angle = 0.075 * math.sin(phase)
    x, y = x * math.cos(angle) - y * math.sin(angle), x * math.sin(angle) + y * math.cos(angle)
    return (925 + 0.88 * x - 0.72 * y, 315 + 0.32 * x + 0.32 * y - 0.94 * z)


def render(phase, font):
    image = Image.new("RGB", (WIDTH * SCALE, HEIGHT * SCALE), GROUND)
    draw = ImageDraw.Draw(image)

    def xy(p):
        return tuple(round(v * SCALE) for v in p)

    def line(points, color, width=1):
        draw.line([xy(p) for p in points], fill=color, width=max(1, round(width * SCALE)), joint="curve")

    def polygon(points, fill, outline=None):
        draw.polygon([xy(p) for p in points], fill=fill)
        if outline:
            line(points + [points[0]], outline)

    def text(position, value, size, color=INK):
        face = ImageFont.truetype(str(font), size * SCALE) if font else ImageFont.load_default(size=size * SCALE)
        draw.text(xy(position), value, font=face, fill=color, stroke_width=0)

    # A static field keeps GIF compression efficient and the diagram readable.
    for x in range(620, 1201, 40):
        line([(x, 34), (x, 406)], (16, 17, 39))
    for y in range(46, 407, 40):
        line([(620, y), (1198, y)], (16, 17, 39))
    line([(48, 46), (112, 46)], ACCENT, 2)
    text((48, 92), "Junrill Galvez", 58)
    text((51, 180), "Senior Software", 34)
    text((51, 223), "Engineer", 34)
    text((51, 290), "System Design · AI Integration", 24, (185, 181, 207))
    line([(51, 364), (499, 364)], (45, 43, 70))
    text((51, 381), "DESIGN THE SYSTEM. CONNECT THE PARTS.", 13, (157, 150, 181))

    def project(point):
        return projection(point, phase)

    def block(center, width, depth, height, top, front, side):
        x, y, z = center
        corners = [(x - width / 2, y - depth / 2, z), (x + width / 2, y - depth / 2, z),
                   (x + width / 2, y + depth / 2, z), (x - width / 2, y + depth / 2, z)]
        upper = [project((a, b, c + height)) for a, b, c in corners]
        lower = [project(p) for p in corners]
        polygon([upper[1], upper[2], lower[2], lower[1]], side, (96, 78, 137))
        polygon([upper[2], upper[3], lower[3], lower[2]], front, (96, 78, 137))
        polygon(upper, top, (157, 134, 207))

    # Projection of a real XYZ scene: layers share a plane, nodes occupy height.
    for z, width, depth in [(0, 275, 204), (29, 244, 177), (58, 211, 150)]:
        block((0, 0, z), width, depth, 12, (42, 35, 65), (28, 24, 47), (35, 29, 56))

    nodes = [(-151, -71, 116), (115, -99, 145), (137, 89, 117)]
    center = (0, 0, 117)
    for index, endpoint in enumerate(nodes):
        elbow = (endpoint[0], 0, 117)
        points = [project(center), project(elbow), project(endpoint)]
        line(points, (103, 83, 145), 1.5)
        progress = (phase / (2 * math.pi) + index / 3) % 1
        segment = progress * 2
        start, end = points[min(int(segment), 1):min(int(segment), 1) + 2]
        blend = segment % 1
        px, py = (start[0] + (end[0] - start[0]) * blend, start[1] + (end[1] - start[1]) * blend)
        draw.ellipse([xy((px - 3, py - 3)), xy((px + 3, py + 3))], fill=(223, 210, 255))

    for index, (x, y, z) in enumerate(nodes):
        float_z = z + 3 * math.sin(phase + index * 2 * math.pi / 3)
        line([project((x, y, 12)), project((x, y, float_z - 12))], (47, 40, 74))
        block((x, y, float_z), 43, 43, 31, (115, 92, 158), (65, 47, 99), (84, 62, 122))
        px, py = project((x, y, float_z + 32))
        draw.ellipse([xy((px - 3, py - 3)), xy((px + 3, py + 3))], fill=INK)

    block((0, 0, 81), 84, 73, 52, (185, 163, 251), (90, 67, 136), (125, 98, 177))
    # Engraved circuit lines follow the upper face instead of a floating badge.
    for y in [-18, 0, 18]:
        line([project((-25, y, 134)), project((25, y, 134))], (223, 209, 255), 1.5)
    line([project((0, -26, 134)), project((0, 26, 134))], (223, 209, 255), 1.5)
    text((805, 389), "CONCEPTUAL ARCHITECTURE", 12, (137, 126, 163))
    return image.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)


def main(args):
    font = font_path(args.font)
    args.output.mkdir(parents=True, exist_ok=True)
    still_path = args.output / "senior-engineer-still.png"
    motion_path = args.output / "senior-engineer-motion.gif"
    first = render(0, font)
    first.save(still_path, optimize=True)
    # One shared palette prevents flicker; exact frame timing is GIF-compatible.
    palette = first.quantize(colors=96, method=Image.Quantize.MEDIANCUT)
    frames = [render(i * 2 * math.pi / FRAMES, font).quantize(palette=palette, dither=Image.Dither.NONE)
              for i in range(FRAMES)]
    frames[0].save(motion_path, save_all=True, append_images=frames[1:], duration=DURATION,
                   loop=0, optimize=True, disposal=1)
    # Verify output format, persistence, loop timing and mathematically closed motion.
    assert max(abs(a - b) for a, b in zip(projection((130, 80, 90), 0), projection((130, 80, 90), 2 * math.pi))) < 1e-9
    assert Image.open(still_path).size == (WIDTH, HEIGHT)
    with Image.open(motion_path) as result:
        assert result.size == (WIDTH, HEIGHT) and result.n_frames == FRAMES
        assert result.info["loop"] == 0 and result.info["duration"] == DURATION
        result.seek(FRAMES - 1)
        result.load()
    assert motion_path.stat().st_size <= 3 * 1024 * 1024, "GIF exceeds 3 MiB"
    for path in [still_path, motion_path]:
        print(f"{path.name}: {WIDTH}×{HEIGHT}, {path.stat().st_size:,} bytes")
    print(f"Self-check passed: {FRAMES} frames, {FRAMES * DURATION / 1000:.1f}s seamless loop")


if __name__ == "__main__":
    args = arguments()
    from PIL import Image, ImageDraw, ImageFont

    main(args)
