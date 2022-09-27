from tkinter import *
from pytube import YouTube
from functools import partial  
root = Tk()
#Decoration
root.geometry("700x400")
root.resizable(0,0)#fixed size
root.title("Youtube Downloader")

#Variables
url=StringVar()
save_path = StringVar()

#Youtube Dowloader functions
def download_vid(url,save_path):
    try:
        yt = YouTube(url)
    except:
        Label(root, text = 'CONNECTION ERROR', font = 'arial 15').place(x= 180 , y = 120)
        
    video = yt.streams.first()
    video.download(save_path)
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 120)  


label_url=Label(root,text="Youtube URL",font="sans-serif 13").place(x=10,y=30)
en_url = Entry(root,width=70,textvariable=url).place(x = 140, y = 30)  
bt_res = Button(root, text = "Get Resolution",activebackground = "light blue", activeforeground = "blue",width=15).place(x = 580, y = 30) 
label_path=Label(root,text="Path",font="sans-serif 13").place(x=10,y=60)
en_path = Entry(root,width=70,textvariable=save_path).place(x = 140, y = 60)
bt_path = Button(root, text = "Browse",activebackground = "light blue", activeforeground = "blue",width=15).place(x = 580, y = 60)
#label_res=Label(root,text="Resolution",font="sans-serif 15").place(x=10,y=90)

#Video Or Audio Botton
bt_vid = Button(root,command=download_vid, text = "Video 480p",activebackground = "light blue", activeforeground = "blue",width=30).place(x = 140, y = 90)
bt_aud = Button(root, text = "Audio mp4",activebackground = "light blue", activeforeground = "blue",width=30).place(x = 380, y = 90)

#Resolution output command=func 


    
     
    



root.mainloop()