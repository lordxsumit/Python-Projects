from dotenv import load_dotenv
from instabot import Bot
import os

load_dotenv()

insta_username = os.getenv("insta_username")
insta_password = os.getenv("insta_password")
insta_friend1 = os.getenv("insta_friend1")
insta_friend2 = os.getenv("insta_friend2")

bot = Bot()

bot.login(username = insta_username, password = insta_password)     # Logging in to instagarm id

# To follow a user
bot.follow('manya_bgmii')

# To follow multiple users
bot.follow_users([insta_friend1, insta_friend2])

# To unfollow a user
bot.unfollow('manya_bgmii')

# To upload a photo
bot.upload_photo("Give here the image link you want to upload", caption="Give here the caption you want to add to you image")

# To upload a video
bot.upload_video("Give here the video link you want to upload", caption="Give here the caption you want to add to your video")

# To send message to a multiple or a single user
bot.send_message("Hello Ji", [insta_friend1, insta_friend2])