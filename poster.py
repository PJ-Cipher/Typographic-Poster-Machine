import argparse
import random
import os
from styles import STYLES, COLORS

def generate(quote, author, style, color, output):
    if style == "random":
        style = random.choice(list(STYLES.keys()))
        print(f"Style: {style}")

    if color.startswith("#"):
        accent = color
    else:
        accent = COLORS.get(color, "#D85A30")

    render_fn = STYLES[style]
    img = render_fn(quote, author, accent)
    img.save(output)
    print(f"Saved → {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a typographic poster from a quote."
    )
    parser.add_argument("quote",              help="The quote to render")
    parser.add_argument("--author",           default="",          help="Attribution line")
    parser.add_argument("--style",            default="editorial",
                        choices=list(STYLES.keys()) + ["random"],  help="Visual style")
    parser.add_argument("--color",            default="coral",
                        help="Accent color: name (coral/blue/teal/pink/amber/purple/black) or hex (#FF0000)")
    parser.add_argument("--output",           default="poster.png", help="Output filename")

    args = parser.parse_args()
    generate(args.quote, args.author, args.style, args.color, args.output)