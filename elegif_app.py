import os

from video import create_text_animation
from music import add_music

# Define the parameters
text_list = [
    "La beauté, c’est véritablement ton rayon.",
    "À tel point que le soleil",
    "C’est toi qui lui fait de l’ombre.",
    "\n- R.D -"
]

fps = 24
video_properties = [1080, 1920, fps]
duration_per_line = 4  # in seconds
background_color = "#FEFEFE"  # Light Grey
text_color = "#454545"  # Dark Grey
colors = [background_color, text_color]
font_file = "ggsans-med.ttf"  # Path to your custom font file
output_dir = "output"
animation = "fade_in"
language = "fr"  # Language code for the desired flag
name = "Rayon_A"  # Name for the output file (optional)
music_file = "music.mp3"  # Path to the music file

#Manage name
file_name = ""
file_count = len([name for name in os.listdir(output_dir) if os.path.isfile(os.path.join(output_dir, name))])
if name != "":
    output_file = os.path.join(output_dir, f"{name}.mp4")
else:
    output_file = os.path.join(output_dir, f"test{file_count + 1}.mp4")

# Create the video
video = create_text_animation(video_properties, text_list, duration_per_line, colors, font_file, output_file, animation, language)

# Add music to the video
video_with_music = video
#video_with_music = add_music(video, music_file)

# Save the video with music to the output directory
video_with_music.write_videofile(output_file, fps=fps, codec="libx264", audio_codec="aac")
