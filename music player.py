import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc
import tkinter as tk
from tkinter import filedialog
from tkinter import *

root = tk.Tk()

root.title("Music Player ♫")
root.geometry('505x462')
root.config(bg = 'gray25')
root.resizable(False,False)

class Player(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.master = master
        self.SONGS = list()
        self.MUSICS = list()
        self.PsePly = '▶'
        self.gui()

    def gui(self):
        self.MusicList = Frame(self.master, height = 374, width = 420, borderwidth = 0, bg = 'gray20')
        self.MusicList.place(x = 90, y = 0)

        self.dirctry = Frame(self.MusicList, height = 30, width = 405, bg = 'gray15', borderwidth = 0)
        self.dirctry.place(x = 10, y = 10)

        self.foldr = Button(self.dirctry, text = '🗀', font = ('impact', 20), fg = 'white', bg = 'gray15',
                            activeforeground = 'orange', activebackground = 'gray15', borderwidth = 0,command = self.askdirctry)
        self.foldr.place(x = 1, y = -17)

        self.fldrnme = Label(self.dirctry, text = '← Choose a folder to look for .mp3 and .wav files.',font =('calibri',8), fg = 'white', bg = 'gray15')
        self.fldrnme.place(x = 40, y = 5)

        self.lbframe = Frame(self.MusicList, borderwidth = 0, height = 500, width = 360, bg = 'gray')
        self.lbframe.place(x= 10, y = 50)

        self.sb = Scrollbar(self.lbframe,elementborderwidth = 0, orient = VERTICAL,bg = 'orange')
        self.sb.pack(side = 'right', fill = 'y')

        self.mlist = Listbox(self.lbframe,fg = 'white',bg = 'gray15', font = ('calibri',10),highlightcolor  = 'orange',
                             selectbackground = 'orange', height = 20,width = 55,bd = 0,yscrollcommand = self.sb.set)
        self.mlist.pack()

        self.sb.config(command = self.mlist.yview)

        self.nomusic = Label(self.MusicList, text = 'Please choose a folder first!', font =('calibri',12), fg = 'white', bg = 'gray15')
        self.nomusic.place(x = 108, y = 190)

        self.playFrame = Frame(self.master, height = 90, width = 505, bg = 'gray45',borderwidth = 0)
        self.playFrame.place(x = 0, y = 372)

        self.pl_time = Label(self.playFrame, text = '00:00', fg = 'white',bg = 'gray45', font =('calibri',8))
        self.pl_time.place(x=90,y=5)

        self.musicFrame = Frame(self.playFrame, height = 90, width = 90,borderwidth = 0)
        self.musicFrame.place(x = 0, y = 0)

        self.music = Label(self.musicFrame, text = '♫',fg = 'gray15', font = ('impact',40))
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
            self.music.config(fg ='orange')
        elif self.PsePly == 'II':
            self.PsePly = '▶'
            self.play.config(text = self.PsePly)
            self.music.config(fg = 'gray15')

    def askdirctry(self):
        self.count = 1
        self.SONGS.clear()
        self.MUSICS.clear()
        self.mlist.delete(0,tk.END)
        self.nomusic.place(x = 108, y = 190)
        self.folderop = filedialog.askdirectory()
        if len(self.folderop) > 65:
            self.foldr.config(fg = 'orange')
            self.fldrnme.config(text = '← ' + self.folderop[0:65]+'...')
        elif len(self.folderop) == 0:
            self.foldr.config(fg = 'white')
            self.fldrnme.config(text = '← Choose a folder to look for .mp3 and .wav files.')
        else:
            self.foldr.config(fg = 'orange')
            self.fldrnme.config(text = '← ' + self.folderop)

        for x in os.listdir(self.folderop):
            if x.endswith('.mp3') or x.endswith('.wav'):
                self.SONGS.append(x)
                self.MUSICS.append("  {0}. {1}".format(self.count,x))
            self.count += 1
        
        if len(self.MUSICS) == 0:
            self.nomusic.config(text = 'No songs found in this folder')
        else:
            for s in self.MUSICS:
                self.nomusic.place_forget()
                self.mlist.insert(END, s)
                self.mlist.config()




        

Player(root).place()

root.mainloop()
