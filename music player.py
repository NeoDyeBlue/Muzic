import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc
import tkinter as tk
from tkinter import filedialog
from tkinter import *

root = tk.Tk()

root.title("Music Player ♫")
root.geometry('460x430')
root.resizable(False,False)

class Player(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.master = master
        self.PsePly = '▶'
        self.gui()

    def gui(self):
        self.playFrame = LabelFrame(self.master, height = 100, width = 460, bg = 'gray45',borderwidth = 0)
        self.playFrame.place(x = 0, y = 340)

        self.pl_time = Label(self.playFrame, text = '00:00', fg = 'white',bg = 'gray45', font =('calibri',8))
        self.pl_time.place(x=90,y=5)

        self.musicFrame = LabelFrame(self.playFrame, height = 80, width = 80,borderwidth = 0)
        self.musicFrame.place(x = 5, y = 5)

        self.music = Label(self.musicFrame, text = '♫',fg = 'orange', font = ('impact',40))
        self.music.place(x = 15, y = 3)
        
        self.play = Button(self.playFrame, text = self.PsePly, font = ('impact',20),fg = 'white', bg = 'gray45',
                           activeforeground = 'orange',activebackground = 'gray45',borderwidth = 0, command = self.pseply)
        self.play.place(x = 245, y = 40)

        self.MusicList = LabelFrame(self.master, height = 330, width = 360, borderwidth = 0, bg = 'gray75')
        self.MusicList.place(x = 100, y = 0)

        self.dirctry = LabelFrame(self.master, height = 30, width = 350, bg = 'gray45', borderwidth = 0)
        self.dirctry.place(x = 110, y = 10)

        self.foldr = Button(self.dirctry, text = '🗀', font = ('impact', 20), fg = 'white', bg = 'gray45',
                            activeforeground = 'orange', activebackground = 'gray45', borderwidth = 0,command = self.askdirctry)
        self.foldr.place(x = 1, y = -17)

        self.fldrnme = Label(self.dirctry, text = '← Choose a directory to look for .mp3 and .wav files.',font =('calibri',8), fg = 'white', bg = 'gray45')
        self.fldrnme.place(x = 40, y = 5)

        self.nomusic = Label(self.MusicList, text = 'Please choose a directory first', font =('calibri',12), fg = 'white', bg = 'gray75')
        self.nomusic.place(x = 78, y = 155)

    def nothing(self):
        pass

    def pseply(self):
        if self.PsePly == '▶':
            self.PsePly = 'II'
            self.play.config(text = self.PsePly)
        elif self.PsePly == 'II':
            self.PsePly = '▶'
            self.play.config(text = self.PsePly)

    def askdirctry(self):
        self.folderop = filedialog.askdirectory()
        if len(self.folderop) > 55:
            self.fldrnme.config(text = '← ' + self.folderop[0:55]+'...')
        elif len(self.folderop) == 0:
            self.fldrnme.config(text = '← Choose a directory to look for .mp3 and .wav files.')
        else:
            self.fldrnme.config(text = '← ' + self.folderop)

        self.mlist = Scrollbar(self.MusicList, borderwidth = 0, orient = VERTICAL)
        self.mlist.place(x = 335, y = 50)

Player(root).place()

root.mainloop()
