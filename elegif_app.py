from video import create_text_animation

text_list = [
    "La beauté, c’est véritablement ton rayon.",
    "Au point que le soleil",
    "C’est toi qui lui fait de l’ombre.",
    "\n- R.D -"
]

duration_per_line = 3.5  # in seconds
background_color = "#FEFEFE"  # Light Grey
text_color = "#454545"  # Dark Grey
colors = [background_color, text_color]
font_file = "ggsans-med.ttf"  # Path to your custom font file
output_dir = "output"
animation = "fade_in"
language = "fr"  # Language code for the desired flag
name = ""  # Name for the output file (optional)

create_text_animation(text_list, duration_per_line, colors, font_file, output_dir, animation, language, name)
