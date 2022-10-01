from tkinter import*
from pytube import YouTube
import os, fnmatch


def submitForm():    
    strFile = optVariable.get()
    # Print the selected value from Option (Combo Box)    
    if (strFile !=''):        
        print('Selected Value is : ' + strFile)

#resString = resolution.get()
#video.yt.streams.filter(res=resString).first().download()
#Label(root, text = 'DOWNLOADED'+resString, font = 'arial 15').place(x= 180 , y = 140)

root = Tk()
root.geometry('500x500')
root.title("Demo Form ")
OP=["OP1",
    "OP2",
    "OP3"]

label_2 = Label(root, text="Choose Files ",width=20,font=("bold", 10))
label_2.place(x=68,y=250)

#flist = fnmatch.filter(os.listdir('.'), '*.mp4')
optVariable = StringVar(root)
optVariable.set([0]) # default value
optFiles = OptionMenu(root,optVariable ,*OP)#*flist
optFiles.pack()
optFiles.place(x=240,y=250)

Button(root, text='Submit', command=submitForm, width=20,bg='brown',fg='white').place(x=180,y=380)
RES_list=["720p","480p","360p","144p"]#list of resoliton
resolution = StringVar(root)
resolution.set(RES_list[1])
menu_resol = OptionMenu(root,resolution , *RES_list)
menu_resol.pack()
menu_resol.place(x =5, y =30)

def awww():
    print("<-----------------------"+resolution.get());
#button(root,text="Download",commad=download_vid,)
btq=Button(root,text="here",command=awww).place(x=10,y=12)
root.mainloop()