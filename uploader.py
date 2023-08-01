import os

import instabot

from elegif.helper import load_credentials

input_vid = 'output/' + 'TestPubliInstagram_A_##.mp4'

print('publish to insta')
bot = instabot.Bot()
username, password = load_credentials("instagram")
bot.login(username=username, password=password)

bot.upload_video(input_vid, caption='caption')

os.remove('config')
