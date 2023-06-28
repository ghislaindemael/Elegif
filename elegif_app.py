import glob
import os

from video import generate_video
from music import add_music

# Set all the parameters

# The poem
name = "Pléiade"
poem = [
    "Je ne comprends pas les gens. Ni ceux qui s’entassent",
    "Pour de la bière tiède dans un bar sombre, mal ventilé,",
    "Ni ceux qui payent un rein pour un siège en terrasse,",
    "Un café soluble accompagné d’un croissant surgelé.",
    "\n",
    "Ce qui confère davantage de satisfaction",
    "C’est un verre de Chartreuse et son parfum enivrant,",
    "Dans la main une des Pléiades, de la Collection",
    "Allongé sur un transat sous leur amas scintillant.",
    "\n",
    "- R.D -"
]

# Video properties
width, height, fps, dur_per_line = 1080, 1920, 24, 4
# Animation properties
anim_type, anim_dur = "fade_in", 2
# Colors
background_color, text_color = "#FEFEFE", "#454545"
# Text properties
font, text_size, intra_line_height = "ggsans-med.ttf", 42, 0.2
# Flag properties
lang, flag_width, flag_height = "fr", 125, 125
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
if anim_type != "":
    output_name += "_A"
if lang != "":
    output_name += f"_{lang.upper()}"
output = os.path.join("output", f"{output_name}.mp4")

# Generate the video
video = generate_video(poem, video_params, anim_params, color_params, text_params, flag_params)

# Add music to the video
video_with_music = video
# video_with_music = add_music(video, music_file)

# Save the video
video_with_music.write_videofile(output, fps=fps, codec="libx264", audio_codec="aac")
