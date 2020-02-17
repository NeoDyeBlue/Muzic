import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')

import vlc
import glob
import tkinter as tk
#from tkinter.ttk import *
from tkinter import *


root = tk.Tk()

root.title("Music Player ⌐■_■")
root.geometry('460x435')
root.resizable(False,False)

class Player(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.master = master
        self.gui()

    def gui(self):
        self.playFrame = LabelFrame(self.master, height = 125, width = 450, bg = 'gray',borderwidth = 0)
        self.playFrame.place(x = 5, y = 305)

        self.pl_time = Label(self.playFrame, text = '00:00', fg = 'white',bg = 'gray', font =('calibri',12))
        self.pl_time.place(x=5,y=5)

        self.musicFrame = LabelFrame(self.playFrame, height = 85, width = 85,borderwidth = 0)
        self.musicFrame.place(x = 5, y = 35)

        self.music = Label(self.musicFrame, text = '♫',fg = 'gray', font = ('impact',40))
        self.music.place(x = 15, y = 3)
        
        self.play = Button(self.playFrame, text = '▶', font = ('impact',20), width = 4,fg = 'white', bg = 'gray',
                           activeforeground = 'orange',activebackground = 'gray',borderwidth = 0)
        self.play.place(x = 230, y = 75)

Player(root).place()

root.mainloop()
