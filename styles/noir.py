from PIL import Image, ImageDraw
from fonts.loader import load
from utils import draw_wrapped, hex_to_rgb, text_block_height

W, H = 600, 840

def render(quote, author, accent_hex):
    img = Image.new("RGB", (W, H), "#141414")
    draw = ImageDraw.Draw(img)
    acc = hex_to_rgb(accent_hex)

    # double border
    pad = 40
    draw.rectangle([pad, pad, W - pad, H - pad], outline=acc, width=1)
    draw.rectangle([pad + 8, pad + 8, W - pad - 8, H - pad - 8], outline="#333333", width=1)

    # large decorative quote mark
    deco_font = load("CormorantGaramond-LightItalic.ttf", 200)
    draw.text((-10, 60), "\u201c", font=deco_font, fill="#2a2a2a")

    # quote text
    quote_font = load("CormorantGaramond-LightItalic.ttf", 54)
    inner_pad = pad + 24
    max_w = W - inner_pad * 2
    lh = 66
    block_h = text_block_height(draw, quote, quote_font, max_w, lh)
    start_y = (H - block_h) // 2
    draw_wrapped(draw, quote, quote_font, inner_pad, start_y, max_w, lh, fill="#F5F0E8")

    # author
    if author:
        author_font = load("SpaceMono-Regular.ttf", 11)
        draw.text((inner_pad, H - pad - 44), f"— {author.upper()}", font=author_font, fill=acc)

    return img