import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from elegif.helper import get_flag_path
from moviepy.editor import ImageSequenceClip


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def gen_vid(poem, video_params, anim_params, color_params, text_params, flag_params):

    # Extract & calculate video properties
    width, height, fps, line_dur = video_params[0], video_params[1], video_params[2], video_params[3]
    line_frames = int(fps * line_dur)

    # Extract anim parameters
    animation, anim_dur = anim_params[0], anim_params[1]
    fade_frames = int(fps * anim_dur)

    # Extract  & calc colors
    bg_color, txt_color = hex_to_rgb(color_params[0]), hex_to_rgb(color_params[2])

    # Extract & calculate text properties
    font_file, font_size, intra_height = text_params[0], text_params[1], text_params[2] + 1
    font = ImageFont.truetype("elegif/fonts/" + font_file, font_size)
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
        flag = np.array(flag)[:, :, [2, 1, 0, 3]]  # Swap R and B channels
        flag = Image.fromarray(flag, "RGBA")
        flag_position = (width - (round(1.5 * flag.width)), text_y - round(1.1 * flag.height))
        if flag_position[1] < 0:
            flag_position = (width - flag.width, text_y)

    # Create a list of frames
    frames = []

    for i, line in enumerate(poem):
        # Create a background image
        image = Image.new("RGB", (width, height), bg_color)
        draw = ImageDraw.Draw(image)

        # Adds a language flag if set
        if flag:
            image.paste(flag, flag_position, mask=flag)

        # Rewrite the previous lines without fade effect
        for j in range(i):
            prev_line = poem[j]
            draw.text((text_x, text_y + line_height * j), prev_line, font=font, fill=txt_color)

        if line != "\n":
            # Add text to the PIL image with fade-in effect
            if animation == "fade_in":
                # Calculate the difference between the background color and desired text color
                color_diff = tuple(txt_color[c] - bg_color[c] for c in range(3))

                # Calculate the text color for each frame
                for k in range(fade_frames):
                    fade_progress = k / fade_frames
                    current_color = tuple(int(bg_color[c] + fade_progress * color_diff[c]) for c in range(3))
                    draw.text((text_x, text_y + line_height * i), line, font=font, fill=current_color)
                    frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                    frames.append(frame)
                # Add the frame without fade effect for the remaining duration
                for _ in range(line_frames - fade_frames):
                    frames.append(frame)
            else:
                draw.text((text_x, text_y + line_height * i), line, font=font, fill=txt_color)
                frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                for _ in range(line_frames):
                    frames.append(frame)

    return ImageSequenceClip(frames, fps=fps)
