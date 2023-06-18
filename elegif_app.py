import glob
import os

from video import generate_video
from music import add_music

# Set all the parameters

# The poem
name = "Rayon_A"
poem = [
    "La beauté, c’est véritablement ton rayon.",
    "À tel point que le soleil",
    "C’est toi qui lui fait de l’ombre.",
    "\n- R.D -"
]

# Video properties
width, height, fps, dur_per_line = 1080, 1920, 24, 4
# Animation properties
anim_type, anim_dur = "fade_in", 2
# Colors
background_color, text_color = "#FEFEFE", "#454545"
# Text properties
font, text_size, intra_line_height = "ggsans-med.ttf", 50, 0.2
# Flag properties
lang, flag_width, flag_height = "fr", 100, 100
# Music properties
music_file, volume = "music.mp3", 10

# The code
video_params = [width, height, fps, dur_per_line]
anim_params = [anim_type, anim_dur]
color_params = [background_color, text_color]
text_params = [font, text_size, intra_line_height]
flag_params = [lang, flag_width, flag_height]
music_params = [music_file, 10]

# Manage file name
file_count = len(glob.glob("output/*.mp4"))
output_name = name if name != "" else f"test{file_count + 1}"
output = os.path.join("output", f"{output_name}.mp4")

# Generate the video
video = generate_video(poem, video_params, anim_params, color_params, text_params, flag_params)

# Add music to the video
video_with_music = video
# video_with_music = add_music(video, music_file)

# Save the video
video_with_music.write_videofile(output, fps=fps, codec="libx264", audio_codec="aac")
