import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from flag_helper import get_flag_path


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def generate_pic(poem, img_params, color_params, text_params, flag_params):
    # Extract & calculate video properties
    width, height = img_params[0], img_params[1]

    # Extract  & calc colors
    bg_color, txt_color = hex_to_rgb(color_params[0]), hex_to_rgb(color_params[1])

    # Extract & calculate text properties
    font_file, font_size, intra_height = text_params[0], text_params[1], text_params[2] + 1
    font = ImageFont.truetype("fonts/" + font_file, font_size)
    line_height = int(font_size * intra_height)
    total_line_height = len(poem) * line_height
    longest_line = max(poem, key=len)
    longest_width, _ = ImageDraw.Draw(Image.new("RGB", (width, height), bg_color)).textsize(longest_line, font=font)
    text_x = round(((width - longest_width) // 2) * 0.75)
    text_y = (height - total_line_height) // 2

    # Generate flag image & properties
    flag = None
    language = flag_params[0]
    if language != "":
        flag = Image.open(get_flag_path(language)).convert("RGBA")
        flag = flag.resize((flag_params[1], flag_params[2]))
        flag_position = (width - (round(1.5 * flag.width)), 50)

    # Generate the image
    image = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(image)

    # Adds a language flag if set
    if flag:
        image.paste(flag, flag_position, mask=flag)

    for i, line in enumerate(poem):
        if line != "\n":
            draw.text((text_x, text_y + line_height * i), line, font=font, fill=txt_color)



    return image
