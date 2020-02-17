import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')

import vlc
import glob
import tkinter as tk
#from tkinter.ttk import *
from tkinter import *


root = tk.Tk()

root.title("Music Player ⌐■_■")
root.geometry('450x400')
root.resizable(False,False)

class Player(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.master = master
        self.gui()

    def gui(self):
        self.playFrame = LabelFrame(self.master, height = 100, width = 440, bg = 'gray')
        self.playFrame.place(x = 5, y = 295)

        self.musicFrame = LabelFrame(self.playFrame, height = 85, width = 85)
        self.musicFrame.place(x = 5, y = 5)

        self.music = Label(self.musicFrame, text = '♫',fg = 'gray', font = ('impact',40))
        self.music.place(x = 15, y = 3)
        
        self.play = Button(self.playFrame, text ='▶', font = ('impact',15), width = 4, bg = 'lightgray')
        self.play.place(x = 228, y = 45)

Player(root).place()

root.mainloop()
