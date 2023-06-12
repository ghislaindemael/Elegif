from PIL import Image, ImageDraw, ImageFont
import imageio
import time

def create_text_gif(text):
    # Split the text into lines using \n as the separator
    lines = text.splitlines()

    # Set up the font and image sizes
    font_size = 20
    line_height = font_size + 5
    image_width = 800
    image_height = 800

    # Create a blank image with a white background
    image = Image.new('RGB', (image_width, image_height), 'white')
    draw = ImageDraw.Draw(image)

    # Load a font
    font = ImageFont.truetype('arial.ttf', font_size)

    # Calculate the total animation duration
    animation_duration = 1  # seconds
    frame_duration = 0.05  # seconds
    pause_duration = 0.5  # seconds

    # Create a list to store the frames of the GIF
    frames = []

    # Loop through each line and create frames
    for i in range(len(lines)):
        # Clear the image by drawing a background square
        draw.rectangle((0, 0, image_width, image_height), fill='white')

        # Calculate the y-position for the current line to vertically center it
        y = (image_height - line_height) // 2

        # Draw the current line on the image
        draw.text((10, y), '\n'.join(lines[:i+1]), font=font, fill='black')

        # Create a new frame by copying the current image
        frame = image.copy()

        # Add the frame to the list
        frames.append(frame)

        # Add a pause frame
        pause_frames = int(pause_duration / frame_duration)
        for _ in range(pause_frames):
            frames.append(frame.copy())

    # Save the frames as a GIF using imageio
    gif_path = 'text_animation.gif'
    imageio.mimsave(gif_path, frames, format='GIF', duration=frame_duration)

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

gif_path = create_text_gif(text_input)
print(f"GIF created: {gif_path}")
