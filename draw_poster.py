#!/usr/bin/env python3
"""Draw the news poster for 25 November 2026.

Build tool only: it runs here to produce entry.png. The graded entry
program is main.py, which copies entry.png to /output/entry.png.
"""

import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
OUT = HERE / "entry.png"

WIDTH = 1024
HEIGHT = 1024
CREAM = (247, 243, 232)
NAVY = (20, 38, 77)
NAVY_LIGHT = (36, 58, 110)
INK = (24, 24, 24)
GREY = (92, 92, 92)
ACCENT = (176, 48, 48)
RULE = (200, 192, 172)

TITLE = "WORLD NEWS"
DATE_LINE = "Wednesday 25 November 2026"
FOOTER = "Six stories that defined the day"

STORIES = [
    (
        "Ukraine confirms strike on Russian ship",
        "Zelenskiy says Kyiv hit a cargo ship in the Gulf of Finland; Norway urges caution.",
    ),
    (
        "Houthis hit Riyadh's tallest tower",
        "Attack on the PIF Tower wounds 11; Saudi Arabia condemns a second strike in a week.",
    ),
    (
        "US jury convicts Huawei of trade theft",
        "Huawei found guilty of conspiracy to steal trade secrets and bank fraud.",
    ),
    (
        "China probes Politburo member Chen Jining",
        "Shock corruption inquiry is announced into the Shanghai party chief.",
    ),
    (
        "Trump pardons Thanksgiving turkeys",
        "Freedom and Feathers are spared at the White House ceremony.",
    ),
    (
        "Senegal regains Africa Cup title",
        "CAS overturns the ruling that gave Morocco the trophy after a chaotic final.",
    ),
]


def load_font(bold, size):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf" if bold
        else "/usr/share/fonts/TTF/DejaVuSans.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default(size=size)


def wrap(draw, text, font, max_width):
    lines = []
    for raw in text.split("\n"):
        words = raw.split()
        current = ""
        for word in words:
            trial = f"{current} {word}".strip()
            if draw.textlength(trial, font=font) <= max_width:
                current = trial
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
    return lines


def draw_poster():
    image = Image.new("RGB", (WIDTH, HEIGHT), CREAM)
    draw = ImageDraw.Draw(image)

    title_font = load_font(True, 72)
    date_font = load_font(False, 34)
    head_font = load_font(True, 34)
    body_font = load_font(False, 27)
    number_font = load_font(True, 30)
    footer_font = load_font(False, 26)

    draw.rectangle([0, 0, WIDTH, 168], fill=NAVY)
    draw.text((48, 26), TITLE, font=title_font, fill=(255, 255, 255))
    draw.text((48, 112), DATE_LINE, font=date_font, fill=(205, 214, 235))
    draw.rectangle([0, 168, WIDTH, 176], fill=ACCENT)

    top = 208
    row_height = 122
    text_x = 132
    text_width = WIDTH - text_x - 48

    for index, (headline, summary) in enumerate(STORIES):
        y = top + index * row_height
        centre = y + 44
        draw.ellipse(
            [48, centre - 30, 108, centre + 30],
            fill=NAVY_LIGHT,
        )
        number = str(index + 1)
        number_width = draw.textlength(number, font=number_font)
        draw.text(
            (78 - number_width / 2, centre - 21),
            number,
            font=number_font,
            fill=(255, 255, 255),
        )
        head_lines = wrap(draw, headline, head_font, text_width)
        line_y = y + 6
        for line in head_lines[:2]:
            draw.text((text_x, line_y), line, font=head_font, fill=INK)
            line_y += 40
        body_lines = wrap(draw, summary, body_font, text_width)
        for line in body_lines[:2]:
            draw.text((text_x, line_y), line, font=body_font, fill=GREY)
            line_y += 34
        if index < len(STORIES) - 1:
            draw.line(
                [48, y + row_height - 12, WIDTH - 48, y + row_height - 12],
                fill=RULE,
                width=2,
            )

    footer_y = top + len(STORIES) * row_height + 18
    footer_width = draw.textlength(FOOTER, font=footer_font)
    draw.text(
        ((WIDTH - footer_width) / 2, footer_y),
        FOOTER,
        font=footer_font,
        fill=GREY,
    )

    image.save(OUT, format="PNG")
    return OUT


if __name__ == "__main__":
    path = draw_poster()
    print(f"wrote {path} ({path.stat().st_size} bytes)")
