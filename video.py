import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from flag_helper import get_flag_path


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def create_text_animation(lines_array, line_duration, color_array, font_file, output_dir, isAnimated, language=None,
                          name=None):
    # Define video properties
    width, height, fps = 1080, 1920, 24
    file_count = len([name for name in os.listdir(output_dir) if os.path.isfile(os.path.join(output_dir, name))])
    if name and name != "":
        output_file = os.path.join(output_dir, f"{name}.mp4")
    else:
        output_file = os.path.join(output_dir, f"test{file_count + 1}.mp4")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    # Color parameters
    bg_color = hex_to_rgb(color_array[0])
    txt_color = hex_to_rgb(color_array[1])

    # Text parameters
    font_size = 50
    font = ImageFont.truetype("fonts/" + font_file, font_size)
    longest_line = max(lines_array, key=len)

    # Fade parameters
    frame_duration = int(fps * line_duration)
    fade_frame_count = int(frame_duration / 2)

    # Build flag image file path if language is provided
    flag_image_file = None
    if language and language != "":
        flag_image_file = get_flag_path(language)

    # Load flag image if image file path is provided
    flag_image = None
    if flag_image_file:
        flag_image = Image.open(flag_image_file).convert("RGBA")

    # Iterate over lines
    for i, line in enumerate(lines_array):
        # Create a blank image with the specified background color
        image = Image.new("RGB", (width, height), bg_color)
        draw = ImageDraw.Draw(image)

        # Calculate the position to align the lines left and center the lines horizontally
        text_y = (height - font_size * len(lines_array)) // 2
        longest_line_width, _ = draw.textsize(longest_line, font=font)
        text_x = round(((width - longest_line_width) // 2) * 0.75)

        # Adds a language flag if set
        if flag_image:
            # Resize flag image to desired dimensions
            flag_image_resized = flag_image.resize((100, 100))

            # Calculate flag position
            flag_position = (width - (round(1.5 * flag_image_resized.width)), text_y - flag_image_resized.height)

            # Adjust flag position if it would clip out of frame
            if flag_position[1] < 0:
                flag_position = (width - flag_image_resized.width, text_y)

            # Paste flag image onto the main image
            image.paste(flag_image_resized, flag_position, mask=flag_image_resized)

        # Rewrite the previous lines without fade effect
        for j in range(i):
            prev_line = lines_array[j]
            draw.text((text_x, text_y + font_size * j), prev_line, font=font, fill=txt_color)

        # Add text to the PIL image with fade-in effect for the current line only
        if isAnimated == "fade_in":
            # Calculate the difference between the background color and desired text color
            color_diff = tuple(txt_color[c] - bg_color[c] for c in range(3))

            # Calculate the text color for each frame
            for k in range(fade_frame_count):
                fade_progress = k / fade_frame_count
                current_color = tuple(int(bg_color[c] + fade_progress * color_diff[c]) for c in range(3))
                draw.text((text_x, text_y + font_size * i), line, font=font, fill=current_color)
                frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                video_writer.write(frame)
            # Write the frame without fade effect for the remaining duration
            for _ in range(frame_duration - fade_frame_count):
                video_writer.write(frame)
        else:
            draw.text((text_x, text_y + font_size * i), line, font=font, fill=txt_color)
            frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            # Write the frame for the entire line duration
            for _ in range(frame_duration):
                video_writer.write(frame)

    # Release the video writer
    video_writer.release()
