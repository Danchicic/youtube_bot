from pytube import YouTube
import datetime


def get_video(url):
    now = datetime.datetime.now()
    name_video = f'{now.strftime("%d-%m-%Y-%H-%M-%S")}.mp3'
    print('start')
    YouTube(url).streams.first().download(filename=name_video)
    print('downloaded')


if __name__ == '__main__':
    get_video('https://www.youtube.com/watch?v=V7-OBq05QW0')
