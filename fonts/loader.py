from PIL import ImageFont
import os

FONTS_DIR = os.path.join(os.path.dirname(__file__))

def load(filename, size):
    path = os.path.join(FONTS_DIR, filename)
    try:
        return ImageFont.truetype(path, size)
    except IOError:
        print(f"Warning: font '{filename}' not found, using default.")
        return ImageFont.load_default()