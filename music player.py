import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc
import tkinter as tk
from tkinter import filedialog
from tkinter import *

root = tk.Tk()

root.title("Music Player ♫")
root.geometry('500x460')
root.config(bg = 'gray25')
root.resizable(False,False)

class Player(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.master = master
        self.MUSICS = list()
        self.PsePly = '▶'
        self.gui()

    def gui(self):
        self.MusicList = LabelFrame(self.master, height = 374, width = 410, borderwidth = 0, bg = 'gray20')
        self.MusicList.place(x = 90, y = 0)

        self.dirctry = LabelFrame(self.MusicList, height = 30, width = 400, bg = 'gray15', borderwidth = 0)
        self.dirctry.place(x = 10, y = 10)

        self.foldr = Button(self.dirctry, text = '🗀', font = ('impact', 20), fg = 'white', bg = 'gray15',
                            activeforeground = 'orange', activebackground = 'gray15', borderwidth = 0,command = self.askdirctry)
        self.foldr.place(x = 1, y = -17)

        self.fldrnme = Label(self.dirctry, text = '← Choose a folder to look for .mp3 and .wav files.',font =('calibri',8), fg = 'white', bg = 'gray15')
        self.fldrnme.place(x = 40, y = 5)

        self.sb = Scrollbar(self.MusicList, orient = VERTICAL)
        self.sb.place(x = 383, y = 50)

        self.mlist = Listbox(self.MusicList,fg = 'white',bg = 'gray15', font = ('calibri',10),highlightcolor  = 'orange',
                             selectbackground = 'orange', height = 20,width = 53,bd = 0,yscrollcommand = self.sb.set)
        self.mlist.place(x = 10, y = 50)

        self.sb.config(command = self.mlist.yview)

        self.nomusic = Label(self.MusicList, text = 'Please choose a folder first!', font =('calibri',12), fg = 'white', bg = 'gray15')
        self.nomusic.place(x = 100, y = 190)

        self.playFrame = LabelFrame(self.master, height = 90, width = 500, bg = 'gray45',borderwidth = 0)
        self.playFrame.place(x = 0, y = 370)

        self.pl_time = Label(self.playFrame, text = '00:00', fg = 'white',bg = 'gray45', font =('calibri',8))
        self.pl_time.place(x=90,y=5)

        self.musicFrame = LabelFrame(self.playFrame, height = 90, width = 90,borderwidth = 0)
        self.musicFrame.place(x = 0, y = 0)

        self.music = Label(self.musicFrame, text = '♫',fg = 'orange', font = ('impact',40))
        self.music.place(x = 20, y = 5)
        
        self.play = Button(self.playFrame, text = self.PsePly, font = ('impact',20),fg = 'white', bg = 'gray45',
                           activeforeground = 'orange',activebackground = 'gray45',borderwidth = 0, command = self.pseply)
        self.play.place(x = 245, y = 40)

    def nothing(self):
        pass

    def pseply(self):
        if self.PsePly == '▶':
            self.PsePly = 'II'
            self.play.config(text = self.PsePly)
            self.music.config(fg ='gray25')
        elif self.PsePly == 'II':
            self.PsePly = '▶'
            self.play.config(text = self.PsePly)
            self.music.config(fg = 'orange')

    def askdirctry(self):
        self.MUSICS.clear()
        self.mlist.delete(0,tk.END)
        self.nomusic.place(x = 100, y = 190)
        self.folderop = filedialog.askdirectory()
        if len(self.folderop) > 55:
            self.fldrnme.config(text = '← ' + self.folderop[0:55]+'...')
        elif len(self.folderop) == 0:
            self.fldrnme.config(text = '← Choose a folder to look for .mp3 and .wav files.')
        else:
            self.fldrnme.config(text = '← ' + self.folderop)

        for x in os.listdir(self.folderop):
            if x.endswith('.mp3') or x.endswith('.wav'):
                self.MUSICS.append(x)
        
        if len(self.MUSICS) == 0:
            self.nomusic.config(text = 'No songs found in this folder')
        else:
            for s in self.MUSICS:
                self.nomusic.place_forget()
                self.mlist.insert(END, s)
                self.mlist.config()




        

Player(root).place()

root.mainloop()
