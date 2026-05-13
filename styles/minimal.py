from PIL import Image, ImageDraw
from fonts.loader import load
from utils import draw_wrapped, hex_to_rgb, text_block_height

W, H = 600, 840

def render(quote, author, accent_hex):
    img = Image.new("RGB", (W, H), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    acc = hex_to_rgb(accent_hex)

    pad = 72
    # small accent dash above quote area
    draw.rectangle([pad, 136, pad + 32, 139], fill=acc)

    # quote
    quote_font = load("PlayfairDisplay-Regular.ttf", 50)
    max_w = W - pad * 2
    lh = 64
    block_h = text_block_height(draw, quote, quote_font, max_w, lh)
    start_y = (H - block_h) // 2
    draw_wrapped(draw, quote, quote_font, pad, start_y, max_w, lh, fill="#111111")

    # author
    if author:
        author_font = load("SpaceMono-Regular.ttf", 13)
        draw.rectangle([pad, H - 118, pad + 32, H - 117], fill=acc)
        draw.text((pad, H - 104), author, font=author_font, fill="#aaaaaa")

    return img