from asyncio.windows_events import NULL
from tkinter import *
from pytube import YouTube



link = input("Enter the link: ")
yt = YouTube(link)
#Title of video
print("Title: ",yt.title)
#Length of the video
print("Length of video: ",yt.length%60,"min")
#printing all the available streams
#print(yt.streams)
#Print Avalible audio format
typ = input("Choose the format:\n [ 1 ] for Video 480p \n [ 2 ] for audio \n")
if( typ == 1):
    yt.streams.filter(res="480p",mime_type="video/mp4").first().download()    
else:
    yt.streams.filter(mime_type="audio/mp4").first().download()    

#itage = input("Type the input itage for target :")
#ys = yt.streams.get_by_itag(itage)

#ys.download(input("Set the destination folder :"))
