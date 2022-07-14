from pytube import YouTube
import os


temp_folder = os.path.join(os.path.dirname(__file__), 'temp')

def download(link: str):
    yt = YouTube(link)
    yt.streams.filter(only_audio=True).desc().first().download(temp_folder)
    return yt.title


def clear_downloads():
    for file in os.listdir(temp_folder):
        os.remove(os.path.join(temp_folder, file))
