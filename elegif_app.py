import os
import sys
import instabot

from helper import *
from picture import generate_pic
from video import generate_video

# Set all the parameters
gen_pic = True
gen_vid = True
share_pic_insta = False
share_vid_insta = False
share_vid_tiktok = False

# The poem
lang = ""
name = "Test"

poem = read_poem_file()
poem.append("\n- R.D -")

# Image properties
i_width, i_height = 1080, 1080
# Video properties
width, height, fps, dur_per_line = 1080, 1920, 24, 2
# Animation properties
anim_type, anim_dur = "fade_in", 1
# Colors
video_bg_color, image_bg_color, text_color = "#FEFEFE", "#FAFAFA", "#454545"
# Text properties
font, text_size, intra_line_height = "ggsans-med.ttf", 52, 0.25
# Flag properties
flag_width, flag_height = 125, 125
# Music properties
music_file, volume = "music.mp3", 10

# The code
image_params = [i_width, i_height]
video_params = [width, height, fps, dur_per_line]
anim_params = [anim_type, anim_dur]
color_params = [video_bg_color, image_bg_color, text_color]
text_params = [font, text_size, intra_line_height]
flag_params = [lang, flag_width, flag_height]
music_params = [music_file, 10]

# Manage file names
if name == "":
    sys.exit()

pic_name = "Poème" + name
if lang != "":
    pic_name += f"_{lang.upper()}"
pic_output = os.path.join("output", f"{pic_name}.png")

vid_name = name
if anim_type != "":
    vid_name += "_A"
if lang != "":
    vid_name += f"_{lang.upper()}"
vid_output = os.path.join("output", f"{vid_name}.mp4")

if gen_pic:
    # Generate the picture
    picture = generate_pic(poem, image_params, color_params, text_params, flag_params)
    picture.save(pic_output)

if gen_vid:
    # Generate the video
    video = generate_video(poem, video_params, anim_params, color_params, text_params, flag_params)

    # Add music to the video
    video_with_music = video
    # video_with_music = add_music(video, music_file)

    # Save the video
    video_with_music.write_videofile(vid_output, fps=fps, codec="libx264", audio_codec="aac")
