from utils import download_callback
from constants import temp_folder
from server import bot
from pytube import YouTube
from telebot import types


@bot.message_handler(content_types=['text'])
def message_handler(message: types.Message):
    if message.text.startswith('https://youtu') and message.from_user.id == 1270570382:
        yt = YouTube(message.text)
        yt.register_on_complete_callback(lambda stream, file_path: download_callback(message, file_path))
        yt.streams.filter(only_audio=True).first().download(temp_folder)
