import textwrap
from PIL import Image, ImageDraw, ImageFont
import imageio

def create_text_gif(text, image_height, image_width):
    # Split the text into lines
    lines = text.splitlines()

    # Set up the font and image sizes
    font_size = 20
    line_height = font_size + 5

    # Create a blank image with a white background
    image = Image.new('RGB', (image_width, image_height), 'white')
    draw = ImageDraw.Draw(image)

    # Load a font
    font = ImageFont.truetype('fonts/ggsans-med.ttf', font_size)

    # Create a list to store the frames of the GIF
    frames = []

    # Loop through each line and create frames
    for i, line in enumerate(lines):
        # Calculate the y-position for the current line
        y = ((image_height/2)) - ((len(lines) - i) * line_height)

        # Draw the current line on the image
        draw.text((50, y), line, font=font, fill='black')

        # Create a new frame by copying the current image
        frame = image.copy()

        # Add the frame to the list
        frames.append(frame)

    # Save the frames as a GIF using imageio
    gif_path = 'text_animation.gif'
    imageio.mimsave(gif_path, frames, type='GIF', duration=2)

    return gif_path


# Example usage
text_input = '''
Je n’ai plus aucune inspiration,
Ni pour écrire, ni pour composer.
Car dans ma tête, de toi j’ai une vision,
Et je passe mes journées à la contempler.
\n
- R.D -
'''

gif_path = create_text_gif(text_input, 800, 800)

print(f"GIF created: {gif_path}")
