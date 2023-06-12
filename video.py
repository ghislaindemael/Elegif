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


def create_text_animation(text_list, duration_per_line, background_color, font_file, output_file):
    # Define video properties
    width, height = 1080, 1920
    fps = 24

    # Create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    # Define font properties
    font_face = cv2.FONT_HERSHEY_SIMPLEX | cv2.FONT_ITALIC
    font_size = 48
    font_thickness = 2

    # Convert background color from hexadecimal to RGB
    background_color = hex_to_rgb(background_color)

    # Load custom font
    font = ImageFont.truetype(font_file, font_size)

    frame_duration = int(fps * duration_per_line)

    # Iterate over time intervals
    for i in range(len(text_list)):
        # Create a blank image with the specified background color
        image = Image.new("RGB", (width, height), background_color)
        draw = ImageDraw.Draw(image)

        # Iterate over lines up to current time
        for j in range(i + 1):
            line = text_list[j]

            # Calculate the position to display the text
            text_size = draw.textsize(line, font=font)

            text_x = (width - text_size[0]) // 2
            text_y = (height - text_size[1] * len(text_list)) // 2 + text_size[1] * j

            # Add text to the PIL image
            draw.text((text_x, text_y), line, font=font, fill=(255, 0, 255))

        # Convert the PIL image to OpenCV format
        frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # Write the frame to the video file multiple times to match the duration
        for _ in range(frame_duration):
            video_writer.write(frame)

    # Release the video writer
    video_writer.release()


# Example usage
text_list = [
    "This is the first line of text.",
    "This is the second line of text.",
    "This is the third line of text."
]
duration_per_line = 2  # in seconds
background_color = "#FEFEFE"  # Grey background color in hexadecimal format
font_file = "fonts/ggsans-med.ttf"  # Path to your custom font file
output_file = "text_animation.mp4"

create_text_animation(text_list, duration_per_line, background_color, font_file, output_file)
