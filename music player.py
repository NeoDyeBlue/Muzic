import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')

import vlc
import glob
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
        self.gui()

    def gui(self):
        """
        self.menubar = Menu(self.master)
        self.pmenu = Menu(self.menubar, tearoff=0)
        self.pmenu.add_command(label="Directory",command = self.nothing)
        self.pmenu.add_separator()
        self.pmenu.add_command(label="Exit", command=self.master.destroy)
        self.menubar.add_cascade(label="Player", menu = self.pmenu)
    
        self.omenu = Menu(self.menubar, tearoff=0)
        self.omenu.add_command(label="Theme",command = self.nothing)
        self.menubar.add_cascade(label="Options",menu = self.omenu)
        self.master.config(menu=self.menubar)
        """
        self.playFrame = LabelFrame(self.master, height = 125, width = 460, bg = 'gray',borderwidth = 0)
        self.playFrame.place(x = 0, y = 330)

        self.pl_time = Label(self.playFrame, text = '00:00', fg = 'white',bg = 'gray', font =('calibri',11))
        self.pl_time.place(x=100,y=3)

        self.musicFrame = LabelFrame(self.playFrame, height = 89, width = 89,borderwidth = 0)
        self.musicFrame.place(x = 5, y = 6)

        self.music = Label(self.musicFrame, text = '♫',fg = 'gray', font = ('impact',40))
        self.music.place(x = 15, y = 3)
        
        self.play = Button(self.playFrame, text = '▶', font = ('impact',20),fg = 'white', bg = 'gray',
                           activeforeground = 'orange',activebackground = 'gray',borderwidth = 0)
        self.play.place(x = 230, y = 50)

        self.MusicList = LabelFrame(self.master, height = 320, width = 360, borderwidth = 0, bg = 'lightgray')
        self.MusicList.place(x = 100, y = 0)

        self.dirctry = LabelFrame(self.master, height = 30, width = 350, bg = 'gray', borderwidth = 0)
        self.dirctry.place(x = 110, y = 10)

        self.foldr = Button(self.dirctry, text = '🗀', font = ('impact', 20), fg = 'white', bg = 'gray',
                            activeforeground = 'orange', activebackground = 'gray', borderwidth = 0,command = self.askdirctry)
        self.foldr.place(x = 1, y = -17)

    def nothing(self):
        pass

    def askdirctry(self):
        self.folderop = filedialog.askdirectory()

Player(root).place()

root.mainloop()
