from moviepy.editor import VideoFileClip, AudioFileClip


def add_music(video_file, music_file):
    video = VideoFileClip(video_file)
    music = AudioFileClip(music_file)

    video_with_music = video.set_audio(music)

    return video_with_music
