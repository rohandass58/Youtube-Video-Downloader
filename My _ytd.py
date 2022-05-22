from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube #pip install pytube3 in terminal

Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name, fg="green")

    else:
        locationError.config(text="Please Choose Folder!!", fg="white")

#donwload video
def DownloadVideo():
    choice = ytdchoices.get(


    )
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Paste Link again!!",fg="red")


    #download function
    select.download(Folder_Name)
    ytdError.config(text="Download Completed!!")



root = Tk()
root.title("Adfree Youtube Downloader")
root.geometry("500x650") #set window
root.columnconfigure(0,weight=1)#set all content in center.
root.configure(bg="seagreen")

#Ytd Link Label
ytdLabel = Label(root, text="Enter the URL of the Video", fg="white", bg="seagreen", font=("jost", 20))
ytdLabel.grid()

#Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root, width=75,textvariable=ytdEntryVar)
ytdEntry.grid()

#Error Msg
ytdError = Label(root,text="Error Msg!!", fg="white", bg="seagreen", font=("jost", 20))
ytdError.grid()


#btn of save file
saveEntry = Button(root, width=10, bg="darkgreen", fg="white",  text="Choose Path", font=("jost", 20), command=openLocation)
saveEntry.grid()

#Error Msg location
locationError = Label(root,text="Error Msg of Path", fg="white", bg="darkgreen" , font=("jost",16))
locationError.grid()

#Download Quality
ytdQuality = Label(root,text="Select Quality",font=("jost",20))
ytdQuality.grid()

#dropdown box
choices = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root, values=choices, font=("jost", 20))
ytdchoices.grid()

#donwload btn
downloadbtn = Button(root, text="Donwload", width=10, bg="red", fg="white",font=("jost", 20),  command=DownloadVideo)
downloadbtn.grid()
 
root.mainloop()
