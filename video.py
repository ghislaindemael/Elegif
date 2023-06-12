import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def hex_to_rgb(hex_color):
    # Remove '#' from the beginning of the hexadecimal color string
    hex_color = hex_color.lstrip('#')

    # Split the hexadecimal color string into RGB components
    r, g, b = hex_color[:2], hex_color[2:4], hex_color[4:]

    # Convert each component from hexadecimal to decimal
    r = int(r, 16)
    g = int(g, 16)
    b = int(b, 16)

    # Return the RGB values as a tuple
    return r, g, b


def create_text_animation(lines_array, line_duration, color_array, font_file, output_dir, animation):
    # Define video properties
    width, height = 1080, 1920
    fps = 30
    file_count = len([name for name in os.listdir(output_dir) if os.path.isfile(os.path.join(output_dir, name))])
    output_file = os.path.join(output_dir, f"test{file_count + 1}.mp4")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    # Color parameters
    bg_color = hex_to_rgb(color_array[0])
    txt_color = hex_to_rgb(color_array[1])

    # Text parameters
    font_size = 55
    font = ImageFont.truetype(font_file, font_size)
    longest_line = max(lines_array, key=len)

    # Fade parameters
    frame_duration = int(fps * line_duration)
    fade_frame_count = int(frame_duration / 2)

    # Iterate over lines
    for i, line in enumerate(lines_array):
        # Create a blank image with the specified background color
        image = Image.new("RGB", (width, height), bg_color)
        draw = ImageDraw.Draw(image)

        # Calculate the position to align the lines left and center the lines horizontally
        text_y = (height - font_size * len(lines_array)) // 2
        longest_line_width, _ = draw.textsize(longest_line, font=font)
        text_x = round(((width - longest_line_width) // 2) * 0.75)

        # Rewrite the previous lines without fade effect
        for j in range(i):
            prev_line = lines_array[j]
            draw.text((text_x, text_y + font_size * j), prev_line, font=font, fill=txt_color)

        # Add text to the PIL image with fade-in effect for the current line only
        if animation == "fade_in":
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


# Example usage
text_list = [
    "This is the first line of text.",
    "This is the second line of text.",
    "This is the third line of text.",
    "\n- R.D -"
]
duration_per_line = 5  # in seconds
background_color = "#FEFEFE"  # Light Grey
text_color = "#454545"  # Dark Grey
colors = [background_color, text_color]
font_file = "fonts/ggsans-med.ttf"  # Path to your custom font file
output_dir = "resultats"
animation = "fade_in"

create_text_animation(text_list, duration_per_line, colors, font_file, output_dir, animation)
