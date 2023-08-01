import os
import shutil
import tempfile


def get_flag_path(language):
    dir_prefix = "elegif/images/flags/"
    if language == "###":
        return dir_prefix + "pirate-waving.png"
    if language == "French":
        return dir_prefix + "fr-waving.png"
    elif language == "German":
        return dir_prefix + "de-waving.png"
    elif language == "English":
        return dir_prefix + "gb-waving.png"
    elif language == "Italian":
        return dir_prefix + "it-waving.png"
    # Add more language codes and corresponding flag image paths as needed
    else:
        return None


def get_inspiration_translation(language):
    if language == "fr" or language == "en" or language == "de":
        return "Inspiration : "
    elif language == "it":
        return "Ispirazione : "
    # Add more language codes and corresponding translation paths as needed
    else:
        return "Inspiration : "


def read_poem_file():
    poem_lines = []
    with open("poem", "r", encoding="utf-8") as file:
        for line in file:
            poem_lines.append(line.strip())
    return poem_lines


def get_hashtags():
    with open("hashtags", "r", encoding="utf-8") as file:
        hashtags = "".join("#" + line.strip() + " " for line in file.readlines())
    return hashtags


def load_credentials(platform):
    with open("elegif/credentials.txt", "r") as file:
        for line in file:
            if line.startswith(platform):
                _, username, password = line.strip().split(":")
                return username, password
    return None, None


def create_copy(og_file_path):
    file_name, file_extension = os.path.splitext(og_file_path)
    new_path = file_name + "_tc" + file_extension
    shutil.copy(og_file_path, new_path)

    return new_path

