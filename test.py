from pytube import YouTube
from sys import argv

link = argv[1]

video = YouTube(link)

print("Video Title: ", video.title)
print("Video Views: ", video.views)

dl = video.streams.get_highest_resolution()
dl.download("./ytdownload")



#COMMITITIITITIITI



#NEW BARNCKKKHGHG