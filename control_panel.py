import tkinter as tk
from tkinter import ttk

def create_generator_tab(tab):
    # Title
    title_label = ttk.Label(tab, text="Elegif Generator", font=("Helvetica", 16, "bold"))
    title_label.pack(pady=20)

    # Title input
    title_frame = ttk.Frame(tab)
    title_frame.pack(pady=10, padx=50)

    title_label = ttk.Label(title_frame, text="Titre :")
    title_label.grid(row=0, column=0, padx=10)

    title_entry = ttk.Entry(title_frame, width=50)  # Set width to 50 characters (350 pixels)
    title_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

    # Poem input
    poem_frame = ttk.Frame(tab)
    poem_frame.pack(pady=10, padx=50, fill=tk.BOTH, expand=True)  # Use fill=tk.BOTH and expand=True

    poem_label = ttk.Label(poem_frame, text="Poème :")
    poem_label.grid(row=0, column=0, padx=10)  # Centered

    poem_entries = []  # List to store poem entry widgets

    def add_poem_line():
        new_poem_entry = ttk.Entry(poem_frame, width=50)  # Set width to 50 characters (350 pixels)
        new_poem_entry.grid(row=len(poem_entries) + 1, column=0, padx=5, pady=5, sticky="ew")
        poem_entries.append(new_poem_entry)
        update_window_size()

    def remove_poem_line():
        if len(poem_entries) > 1:
            last_poem_entry = poem_entries.pop()
            last_poem_entry.destroy()
            update_window_size()

    def update_window_size():
        root.update_idletasks()  # Update the window immediately before calculating size
        total_height = sum(entry.winfo_reqheight() for entry in poem_entries) + 280
        total_width = min(400, max(entry.winfo_reqwidth() for entry in poem_entries) + 120)
        root.geometry(f"{total_width}x{total_height}")

    poem_entry = ttk.Entry(poem_frame, width=50)  # Set width to 50 characters (350 pixels)
    poem_entry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    poem_entries.append(poem_entry)

    # +/- Buttons
    buttons_frame = ttk.Frame(tab)
    buttons_frame.pack(pady=10)

    plus_button = ttk.Button(buttons_frame, text="+", command=add_poem_line)
    plus_button.grid(row=0, column=0, padx=5)

    minus_button = ttk.Button(buttons_frame, text="-", command=remove_poem_line)
    minus_button.grid(row=0, column=1, padx=5)

def create_publisher_tab(tab):
    # Add widgets for poem publishing
    pass

def create_window():
    global root  # Make root a global variable so it can be accessed from other functions
    root = tk.Tk()
    root.title("Poem Editor")
    root.geometry("500x400")

    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True)

    generator_tab = ttk.Frame(notebook)
    publisher_tab = ttk.Frame(notebook)

    notebook.add(generator_tab, text="Generator")
    notebook.add(publisher_tab, text="Publisher")

    create_generator_tab(generator_tab)
    create_publisher_tab(publisher_tab)

    root.mainloop()

if __name__ == "__main__":
    create_window()
