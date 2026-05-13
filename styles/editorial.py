from PIL import Image, ImageDraw
from fonts.loader import load
from utils import draw_wrapped, hex_to_rgb, text_block_height

W, H = 600, 840

def render(quote, author, accent_hex):
    img = Image.new("RGB", (W, H), "#FAFAF7")
    draw = ImageDraw.Draw(img)
    acc = hex_to_rgb(accent_hex)

    # top rule bar
    draw.rectangle([0, 0, W, 8], fill=acc)

    # label
    label_font = load("SpaceMono-Regular.ttf", 11)
    draw.text((48, 50), "TYPOGRAPHIC POSTER", font=label_font, fill="#111111")
    draw.rectangle([48, 68, 108, 70], fill=acc)

    # quote
    quote_font = load("PlayfairDisplay-BoldItalic.ttf", 60)
    pad = 48
    max_w = W - pad * 2
    lh = 74
    block_h = text_block_height(draw, quote, quote_font, max_w, lh)
    start_y = (H - block_h) // 2 - 20
    draw_wrapped(draw, quote, quote_font, pad, start_y, max_w, lh, fill="#111111")

    # author
    if author:
        author_font = load("SpaceMono-Regular.ttf", 13)
        draw.rectangle([48, H - 108, W - 48, H - 107], fill="#dddddd")
        draw.text((48, H - 88), f"— {author.upper()}", font=author_font, fill="#888888")

    return img