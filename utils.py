def wrap_text(draw, text, font, max_width):
    """Split text into lines that fit within max_width."""
    words = text.split()
    lines = []
    line = ""

    for word in words:
        test_line = line + word + " "
        width = draw.textlength(test_line, font=font)
        if width > max_width and line:
            lines.append(line.strip())
            line = word + " "
        else:
            line = test_line

    if line:
        lines.append(line.strip())

    return lines


def draw_wrapped(draw, text, font, x, y, max_width, line_height, fill="black", align="left"):
    """Draw wrapped text and return how many lines were drawn."""
    lines = wrap_text(draw, text, font, max_width)

    for i, line in enumerate(lines):
        line_y = y + i * line_height
        if align == "center":
            line_width = draw.textlength(line, font=font)
            x_pos = x - line_width / 2
        else:
            x_pos = x
        draw.text((x_pos, line_y), line, font=font, fill=fill)

    return len(lines)


def hex_to_rgb(hex_color):
    """Convert '#D85A30' to (216, 90, 48)."""
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def text_block_height(draw, text, font, max_width, line_height):
    """Calculate total pixel height of a wrapped text block."""
    lines = wrap_text(draw, text, font, max_width)
    return len(lines) * line_height