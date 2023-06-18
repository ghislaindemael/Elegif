def get_flag_path(language):
    dir_prefix = "images/flags/256/"
    if language == "fr":
        return dir_prefix + "France-flag.png"
    elif language == "de":
        return dir_prefix + "Germany-flag.png"
    # Add more language codes and corresponding flag image paths as needed
    else:
        return None