from PIL import Image, ImageDraw
from fonts.loader import load
from utils import draw_wrapped, hex_to_rgb, text_block_height
import datetime

W, H = 600, 840

def render(quote, author, accent_hex):
    img = Image.new("RGB", (W, H), "#F7F0DC")
    draw = ImageDraw.Draw(img)
    acc = hex_to_rgb(accent_hex)
    border = (139, 111, 71)

    # decorative double border
    b = 24
    draw.rectangle([b, b, W - b, H - b], outline=border, width=3)
    draw.rectangle([b + 8, b + 8, W - b - 8, H - b - 8], outline=border, width=1)

    # header label
    label_font = load("SpaceMono-Bold.ttf", 10)
    year = datetime.datetime.now().year
    label = f"EST. {year}"
    lw = draw.textlength(label, font=label_font)
    draw.text(((W - lw) // 2, 70), label, font=label_font, fill=border)
    draw.rectangle([(W // 2) - 60, 90, (W // 2) + 60, 93], fill=acc)

    # quote centered
    quote_font = load("CormorantGaramond-SemiBoldItalic.ttf", 52)
    max_w = W - 120
    lh = 66
    block_h = text_block_height(draw, quote, quote_font, max_w, lh)
    start_y = (H - block_h) // 2
    draw_wrapped(draw, quote, quote_font, W // 2, start_y, max_w, lh,
                 fill="#2C1810", align="center")

    # separator + author
    draw.rectangle([(W // 2) - 60, H - 142, (W // 2) + 60, H - 140], fill=acc)
    if author:
        author_font = load("SpaceMono-Regular.ttf", 12)
        label = f"— {author.upper()} —"
        lw = draw.textlength(label, font=author_font)
        draw.text(((W - lw) // 2, H - 110), label, font=author_font, fill=border)

    return img