from PIL import Image, ImageDraw
from fonts.loader import load
from utils import draw_wrapped, hex_to_rgb, text_block_height

W, H = 600, 840

def render(quote, author, accent_hex):
    img = Image.new("RGB", (W, H), "#F2F0E8")
    draw = ImageDraw.Draw(img)
    acc = hex_to_rgb(accent_hex)

    # thick left bar
    draw.rectangle([0, 0, 12, H], fill=acc)

    # quote in heavy caps
    quote_font = load("Anton-Regular.ttf", 76)
    lpad, pad = 28, 36
    max_w = W - pad - lpad
    lh = 82
    block_h = text_block_height(draw, quote.upper(), quote_font, max_w, lh)
    start_y = (H - block_h) // 2 + 20
    draw_wrapped(draw, quote.upper(), quote_font, lpad, start_y, max_w, lh, fill="#111111")

    # accent underline
    draw.rectangle([lpad, H - 148, lpad + 180, H - 142], fill=acc)

    # author
    if author:
        author_font = load("SpaceMono-Bold.ttf", 14)
        draw.text((lpad, H - 108), author.upper(), font=author_font, fill="#111111")

    # outer border
    draw.rectangle([0, 0, W - 1, H - 1], outline="#111111", width=3)

    return img
    