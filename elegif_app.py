import os
import tkinter as tk
from tkinter import ttk
from elegif.picture import gen_pic
from elegif.video import gen_vid


def create_generator_tab(tab):
    # Title
    title_label = ttk.Label(tab, text="Elegif Generator", font=("Helvetica", 16, "bold"))
    title_label.pack(pady=20)

    # Title input
    title_frame = ttk.Frame(tab)
    title_frame.pack(pady=5, padx=50)

    title_label = ttk.Label(title_frame, text="Title :")
    title_label.grid(row=0, column=0, padx=10)

    title_entry = ttk.Entry(title_frame, width=50)  # Set width to 50 characters (350 pixels)
    title_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

    # Language input
    language_frame = ttk.Frame(tab)
    language_frame.pack(pady=5, padx=50)

    language_label = ttk.Label(language_frame, text="Language :")
    language_label.grid(row=0, column=0, padx=10)

    languages = ["French", "English", "German", "Italian", "###"]  # Languages to choose from
    language_var = tk.StringVar()
    language_var.set("###")  # Default value is "###"

    language_dropdown = ttk.Combobox(language_frame, textvariable=language_var, values=languages, state="readonly")
    language_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

    # Poem input
    poem_frame = ttk.Frame(tab)
    poem_frame.pack(pady=0, padx=50, fill=tk.X, expand=False)  # Use fill=tk.BOTH and expand=True

    poem_label = ttk.Label(poem_frame, text="Poem :")
    poem_label.grid(row=0, column=0, padx=10)  # Centered

    poem_entries = []  # List to store poem entry widgets

    def add_poem_line():
        new_poem_entry = ttk.Entry(poem_frame, width=50)  # Set width to 50 characters (350 pixels)
        new_poem_entry.grid(row=len(poem_entries) + 1, column=0, padx=5, pady=0, sticky="ew")
        poem_entries.append(new_poem_entry)
        update_window_size()

    def remove_poem_line():
        if len(poem_entries) > 1:
            last_poem_entry = poem_entries.pop()
            last_poem_entry.destroy()
            update_window_size()

    def update_window_size():
        root.update_idletasks()  # Update the window immediately before calculating size
        total_height = 20 * len(poem_entries) + 375
        total_width = 400
        root.geometry(f"{total_width}x{total_height}")

    poem_entry = ttk.Entry(poem_frame, width=50)  # Set width to 50 characters (350 pixels)
    poem_entry.grid(row=1, column=0, padx=5, pady=0, sticky="ew")
    poem_entries.append(poem_entry)

    # +/- Buttons
    buttons_frame = ttk.Frame(tab)
    buttons_frame.pack(pady=10)

    plus_button = ttk.Button(buttons_frame, text="+", command=add_poem_line)
    plus_button.grid(row=0, column=0, padx=5)

    minus_button = ttk.Button(buttons_frame, text="-", command=remove_poem_line)
    minus_button.grid(row=0, column=1, padx=5)

    # Extra properties section
    extra_properties_frame = ttk.Frame(tab)
    extra_properties_frame.pack(pady=10)

    # Flag Size
    flag_size_label = ttk.Label(extra_properties_frame, text="Flag Size:")
    flag_size_label.grid(row=0, column=0, padx=5)
    flag_size_var = tk.IntVar()
    flag_size_var.set(120)
    flag_size_entry = ttk.Entry(extra_properties_frame, textvariable=flag_size_var, width=6)
    flag_size_entry.grid(row=0, column=1, padx=5)

    # Duration per line
    duration_label = ttk.Label(extra_properties_frame, text="Duration per Line:")
    duration_label.grid(row=0, column=2, padx=5)
    duration_var = tk.DoubleVar()
    duration_var.set(3)
    duration_entry = ttk.Entry(extra_properties_frame, textvariable=duration_var, width=6)
    duration_entry.grid(row=0, column=3, padx=5)

    # Animated Checkbox
    animated_label = ttk.Label(extra_properties_frame, text="Animated")
    animated_label.grid(row=0, column=4, padx=5)
    animated_var = tk.BooleanVar()
    animated_var.set(True)  # Default value is True
    animated_checkbox = ttk.Checkbutton(extra_properties_frame, variable=animated_var)
    animated_checkbox.grid(row=0, column=5, padx=5)

    # Anim Duration
    anim_duration_label = ttk.Label(extra_properties_frame, text="Anim Dur:")
    anim_duration_label.grid(row=1, column=4, padx=5)
    anim_duration_var = tk.DoubleVar()
    anim_duration_var.set(2)
    anim_duration_entry = ttk.Entry(extra_properties_frame, textvariable=anim_duration_var, width=6)
    anim_duration_entry.grid(row=1, column=5, padx=5)

    # Text Size
    text_size_label = ttk.Label(extra_properties_frame, text="Text Size:")
    text_size_label.grid(row=1, column=0, padx=5)
    text_size_var = tk.IntVar()
    text_size_var.set(50)
    text_size_entry = ttk.Entry(extra_properties_frame, textvariable=text_size_var, width=6)
    text_size_entry.grid(row=1, column=1, padx=5)

    # Intra-line Height
    intra_line_label = ttk.Label(extra_properties_frame, text="Intra-line Height:")
    intra_line_label.grid(row=1, column=2, padx=5)
    intra_line_var = tk.DoubleVar()
    intra_line_var.set(0.25)
    intra_line_entry = ttk.Entry(extra_properties_frame, textvariable=intra_line_var, width=6)
    intra_line_entry.grid(row=1, column=3, padx=5)

    def extract_properties():
        # The poem
        lang = language_var.get()
        name = title_entry.get()

        poem = [entry.get() for entry in poem_entries]
        poem.append("\n- R.D -")

        # Image properties
        i_width, i_height = 1080, 1080
        # Video properties
        width, height, fps, dur_per_line = 1080, 1920, 24, duration_var.get()
        # Animation properties
        anim_type, anim_dur = "fade_in" if animated_var.get() else "", anim_duration_var.get()
        # Colors
        video_bg_color, image_bg_color, text_color = "#FEFEFE", "#FAFAFA", "#454545"
        # Text properties
        font, text_size, intra_line_height = "ggsans-med.ttf", text_size_var.get(), intra_line_var.get()
        # Flag properties
        flag_width, flag_height = flag_size_var.get(), flag_size_var.get()

        pic_name = "Poème" + name
        if lang != "":
            pic_name += f"_{lang[0:2].upper()}"
        pic_output = os.path.join("output", f"{pic_name}.png")

        vid_name = name
        if anim_type != "":
            vid_name += "_A"
        if lang != "":
            vid_name += f"_{lang[0:2].upper()}"
        vid_output = os.path.join("output", f"{vid_name}.mp4")

        return [[lang, name, poem, pic_output, vid_output], [i_width, i_height], [width, height, fps, dur_per_line],
                [anim_type, anim_dur], [video_bg_color, image_bg_color, text_color],
                [font, text_size, intra_line_height], [lang, flag_width, flag_height]]

    def generate_pic():
        prop = extract_properties()
        if prop[0][1] != "":
            picture = gen_pic(prop[0][2], prop[1], prop[4], prop[5], prop[6])
            picture.save(prop[0][3])

    def generate_vid():
        prop = extract_properties()
        if prop[0][1] != "":
            video = gen_vid(prop[0][2], prop[2], prop[3], prop[4], prop[5], prop[6])
            video.write_videofile(prop[0][4], fps=prop[2][2], codec="libx264", audio_codec="aac")

    # Generate Picture and Generate Video buttons
    generate_buttons_frame = ttk.Frame(tab)
    generate_buttons_frame.pack(pady=10)

    generate_picture_button = ttk.Button(generate_buttons_frame, text="Generate Picture", command=generate_pic)
    generate_picture_button.pack(side=tk.LEFT, padx=5)

    generate_video_button = ttk.Button(generate_buttons_frame, text="Generate Video", command=generate_vid)
    generate_video_button.pack(side=tk.LEFT, padx=5)

    update_window_size()


def create_publisher_tab():
    # Add widgets for poem publishing
    pass


def create_window():
    global root
    root = tk.Tk()
    root.title("Poem Editor")
    root.geometry("400x350")
    root.resizable(False, False)

    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True)

    generator_tab = ttk.Frame(notebook)
    publisher_tab = ttk.Frame(notebook)

    notebook.add(generator_tab, text="Generator")
    notebook.add(publisher_tab, text="Publisher")

    create_generator_tab(generator_tab)
    create_publisher_tab()

    root.mainloop()


if __name__ == "__main__":
    create_window()
