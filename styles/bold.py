from PIL import Image, ImageDraw
from fonts.loader import load
from utils import draw_wrapped, hex_to_rgb, text_block_height

W, H = 600, 840

def render(quote, author, accent_hex):
    acc = hex_to_rgb(accent_hex)
    img = Image.new("RGB", (W, H), acc)
    draw = ImageDraw.Draw(img)

    # giant decorative quote mark (faded)
    deco_font = load("Anton-Regular.ttf", 320)
    draw.text((-20, 40), "\u201c", font=deco_font, fill=tuple(max(0, c - 40) for c in acc))

    # quote in heavy caps
    quote_font = load("Anton-Regular.ttf", 88)
    pad = 40
    max_w = W - pad * 2
    lh = 94
    block_h = text_block_height(draw, quote.upper(), quote_font, max_w, lh)
    start_y = (H - block_h) // 2
    draw_wrapped(draw, quote.upper(), quote_font, pad, start_y, max_w, lh, fill="#FFFFFF")

    # author
    if author:
        author_font = load("SpaceMono-Regular.ttf", 13)
        draw.text((pad, H - 64), f"— {author}", font=author_font, fill=(255, 255, 255, 160))

    return img