from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.filedialog import FileDialog, askopenfile
from pytube import YouTube
root = Tk()

#author: Elyasse-d
#Version 0.0.1

#Decoration
jls_extract_var = root
jls_extract_var.geometry("700x400")
root.resizable(0,0)#fixed size
root.title("Youtube Downloader")

#Variables54
url=StringVar()
save_path = StringVar()
my_path = StringVar()
resolution=StringVar()

#Youtube Dowloader functions
def download_vid():
    yt = YouTube(str(url.get()))
    try:
        yt = YouTube(str(url.get()))
    except:
        Label(root, text = 'CONNECTION ERROR', font = 'arial 15').place(x= 180 , y = 120)
        
    resString = resolution.get()
    yt.streams.filter(res=resString,file_extension='mp4').first().download(str(my_path.get()))
    Label(root, text = 'DOWNLOADED :'+resString, font = 'arial 15').place(x= 180 , y = 140)  
def download_audio():
    yt = YouTube(str(url.get()))
    try:
        yt = YouTube(str(url.get()))
    except:
        Label(root, text = 'CONNECTION ERROR', font = 'arial 15').place(x= 180 , y = 120)
        
    res_adu_String = resolution_audio.get()
    yt.streams.filter(abr=res_adu_String,only_audio=True).first().download(str(my_path.get()))
    Label(root, text = 'DOWNLOADED :'+res_adu_String, font = 'arial 15').place(x= 180 , y = 140)  

def open_File():
    return filedialog.askdirectory()
def Get_val():
    path = open_File()
    my_path.set(path)
     

label_url=Label(root,text="Youtube URL",font="sans-serif 13").place(x=10,y=30)
en_url = Entry(root,width=70,textvariable=url).place(x = 140, y = 30)  
#bt_res = Button(root, text = "Get Resolution",activebackground = "light blue", activeforeground = "blue",width=15).place(x = 580, y = 30)
#menu_res= Menubutton(root, text = "Resolution", relief = RAISED,padx=5,pady=5) 
#menu_res=OptionMenu(root,variable=resolution,value=resolution)

label_path=Label(root,text="Path",font="sans-serif 13").place(x=10,y=60)
#en_path = Entry(root,width=70,textvariable=save_path).place(x = 140, y = 60)
en_path = Label(root,width=70,textvariable=my_path).place(x = 140, y = 60)

bt_path = Button(root,command=Get_val, text = "Browse",activebackground = "light blue", activeforeground = "blue",width=15).place(x = 580, y = 60)
#label_res=Label(root,text="Resolution",font="sans-serif 15").place(x=10,y=90)

#Video Or Audio Botton
bt_vid = Button(root,command=download_vid, text = "Video",activebackground = "light blue", activeforeground = "blue",width=30).place(x = 140, y = 90)
bt_aud = Button(root,command=download_audio, text = "Audio mp4",activebackground = "light blue", activeforeground = "blue",width=30).place(x = 380, y = 90)


#Resolution output for Video
RES_list=["720p","480p","360p","144p"]#list of resoliton
resolution = StringVar(root)
resolution.set(RES_list[1])
menu_resol = OptionMenu(root,resolution , *RES_list)
menu_resol.pack()
menu_resol.place(x =580, y =30)
#Resolution output for Audio
RES_audio_list=["160kbps","128kbps","70kbps"]#list of resoliton
resolution_audio = StringVar(root)
resolution_audio.set(RES_audio_list[0])
menu_audio_resol = OptionMenu(root,resolution_audio , *RES_audio_list)
menu_audio_resol.pack()
menu_audio_resol.place(x =590, y =10)



root.mainloop()