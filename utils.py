# utils.py

import textwrap
from PIL import ImageDraw

def wrap_text(text, font, draw, max_width):
    """Wrap text to fit within the specified width."""
    wrapped_lines = []
    for line in text.split('\n'):
        words = line.split()
        wl = ""
        for word in words:
            test_line = wl + " " + word if wl else word
            # Check the width of the line with the new word
            if draw.textbbox((0, 0), test_line, font=font)[2] <= max_width:
                wl = test_line
            else:
                if wl:  # add the line without the new word
                    wrapped_lines.append(wl)
                wl = word  # start a new line with the new word
        if wl:  # add the last line
            wrapped_lines.append(wl)
    return '\n'.join(wrapped_lines)

def calculate_text_height(text, font, draw, max_width):
    """Calculate the height of the wrapped text."""
    wrapped_text = wrap_text(text, font, draw, max_width)
    return draw.textbbox((0, 0), wrapped_text, font=font)[3]
