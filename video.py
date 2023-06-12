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


def create_text_animation(lines_array, line_duration, color_array, font_file, output_file):
    # Define video properties
    width, height = 1080, 1920
    fps = 24

    # Create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    # Color parameters
    background_color = hex_to_rgb(color_array[0])
    text_color = hex_to_rgb(color_array[1])

    # Font parameters
    font_size = 55
    font = ImageFont.truetype(font_file, font_size)

    frame_duration = int(fps * line_duration)

    # Find the longest line in the text list
    longest_line = max(lines_array, key=len)

    # Iterate over time intervals
    for i in range(len(lines_array)):
        # Create a blank image with the specified background color
        image = Image.new("RGB", (width, height), background_color)
        draw = ImageDraw.Draw(image)

        # Calculate the position to align the lines left and center the lines horizontally
        text_y = (height - font_size * len(lines_array)) // 2
        longest_line_width, _ = draw.textsize(longest_line, font=font)
        text_x = round(
            ((width - longest_line_width) // 2) * 0.75)  # Set x-coordinate to center align based on the longest line

        # Add text to the PIL image
        for j in range(i + 1):
            line = lines_array[j]
            draw.text((text_x, text_y + font_size * j), line, font=font, fill=text_color)

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
    "This is the third line of text.",
    "\n- R.D - "
]
duration_per_line = 3  # in seconds
background_color = "#FEFEFE"  # Light Grey
text_color = "#454545"  # Dark Grey
colors = [background_color, text_color]
font_file = "fonts/ggsans-med.ttf"  # Path to your custom font file
output_file = "resultats/text_animation.mp4"

create_text_animation(text_list, duration_per_line, colors, font_file, output_file)
