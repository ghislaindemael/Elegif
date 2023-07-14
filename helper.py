def get_flag_path(language):
    dir_prefix = "images/flags/"
    if language == "fr":
        return dir_prefix + "fr-waving.png"
    elif language == "de":
        return dir_prefix + "de-waving.png"
    elif language == "en":
        return dir_prefix + "gb-waving.png"
    elif language == "it":
        return dir_prefix + "it-waving.png"
    # Add more language codes and corresponding flag image paths as needed
    else:
        return None


def read_poem_file():
    poem_lines = []
    with open("poem", "r", encoding="utf-8") as file:
        for line in file:
            poem_lines.append(line.strip())
    return poem_lines
