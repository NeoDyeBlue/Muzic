import tkinter as tk
from tkinter import filedialog
from tkinter import *
import eyed3
import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc

root = tk.Tk()
root.title("Music Player ♫")
root.geometry('508x470')
root.config(bg = 'gray25')
root.resizable(False,False)

class Player(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.master = master
        self.master.bind('<Return>')
        self.MUSICS = list()
        self.PsePly = '▶'
        self.gui()

    def gui(self):
        self.MListframe = Frame(self.master, height = 374, width = 420, borderwidth = 0, bg = 'gray20')
        self.MListframe.place(x = 94, y = 0)

        self.dirframe = Frame(self.MListframe, height = 30, width = 405, bg = 'gray45', borderwidth = 0)
        self.dirframe.place(x = 10, y = 10)

        self.foldr = Button(self.dirframe, text = '🗀', font = ('impact', 20), fg = 'white', bg = 'gray45',
                            activeforeground = 'cyan', activebackground = 'gray45', borderwidth = 0,command = self.askdirctry)
        self.foldr.place(x = 1, y = -17)

        self.fldrnme = Label(self.dirframe, text = '← Choose a folder to look for .mp3 and .wav files.',font =('calibri',8), fg = 'white', bg = 'gray45')
        self.fldrnme.place(x = 40, y = 5)

        self.lbframe = Frame(self.MListframe, borderwidth = 0, height = 500, width = 360, bg = 'gray')
        self.lbframe.place(x= 10, y = 40)

        self.sb = Scrollbar(self.lbframe, orient = VERTICAL,bg = 'deepskyblue')
        self.sb.pack(side = 'right', fill = 'y')

        self.mlist = Listbox(self.lbframe,fg = 'white',bg = 'gray15', font = ('calibri',10),highlightcolor  = 'deepskyblue',
                             selectbackground = 'deepskyblue4', height = 20,width = 55,bd = 0,yscrollcommand = self.sb.set)
        self.mlist.pack()

        self.sb.config(command = self.mlist.yview)

        self.nomusic = Label(self.MListframe, text = 'Please choose a folder first!', font =('calibri',12), fg = 'white', bg = 'gray15')
        self.nomusic.place(x = 108, y = 190)

        self.playFrame = Frame(self.master, height = 62, width = 508, bg = 'gray45',borderwidth = 0)
        self.playFrame.place(x = 0, y = 372)

        self.play = Button(self.playFrame, text = self.PsePly, font = ('impact',20),fg = 'white', bg = 'gray45',
                           activeforeground = 'deepskyblue',activebackground = 'gray45',borderwidth = 0, command = self.pseply)
        self.play.place(x = 274, y = 50)
        
        self.progress = Frame(self.playFrame, borderwidth = 0, height = 27, width = 505,bg = 'gray45' )
        self.progress.place(x = 0, y = 0)
        self.pl_time = Label(self.progress, text = '00:00', fg = 'white',bg = 'gray45', font =('calibri',8))
        self.pl_time.place(x=95,y=5)

        self.current_songFrame = Frame(self.playFrame, borderwidth = 0, height = 42, width = 508,bg = 'gray15' )
        self.current_songFrame.place(x = 0, y = 20)
        self.Artist = Label(self.current_songFrame, text = 'Artist', font = ('calibri',10,), fg = 'white', bg = 'gray15')
        self.Artist.place(x = 95, y = 19)
        self.Songname = Label(self.current_songFrame, text = 'Song Name', font = ('calibri',12,'bold'), fg = 'white', bg = 'gray15')
        self.Songname.place(x = 95, y = -1)

        self.MPbuttonsFrame = Frame(self.master, height = 28, width = 508, bg = 'gray45')
        self.MPbuttonsFrame.place(x = 0, y = 438)

        self.MusicNoteFrame = Frame(self.master, height = 94, width = 94,borderwidth = 0)
        self.MusicNoteFrame.place(x = 0, y = 372)

        self.music = Label(self.MusicNoteFrame, text = '♫',fg = 'gray15', font = ('impact',40))
        self.music.place(x = 22, y = 8)

    

    def nothing(self):
        pass

    def pseply(self):
        if self.PsePly == '▶':
            self.PsePly = 'I I'
            self.play.config(text = self.PsePly, font = ('impact',15))
            self.play.place(x = 278, y = 61)
            self.music.config(fg ='deepskyblue4')
        elif self.PsePly == 'I I':
            self.PsePly = '▶'
            self.play.config(text = self.PsePly, font = ('impact',20))
            self.play.place(x = 274, y = 50)
            self.music.config(fg = 'gray15')

    def askdirctry(self):
        self.MUSICS.clear()
        self.mlist.delete(0,tk.END)
        self.nomusic.place(x = 108, y = 190)
        self.folderop = filedialog.askdirectory()

        if not self.folderop:
            self.foldr.config(fg = 'white')
            self.fldrnme.config(text = '← Choose a folder to look for .mp3 and .wav files.')
        else:
            if len(self.folderop) > 65:
                self.foldr.config(fg = 'cyan')
                self.fldrnme.config(text = '← ' + self.folderop[0:65]+'...')
            else:
                self.foldr.config(fg = 'cyan')
                self.fldrnme.config(text = '← ' + self.folderop)

            for x in os.listdir(self.folderop):
                if x.endswith('.mp3') or x.endswith('.wav'):
                    self.MUSICS.append(x)
       
            if len(self.MUSICS) == 0:
                self.foldr.config(fg = 'white')
                self.nomusic.config(text = 'No songs found in this folder')
            else:
                for s in self.MUSICS:
                    self.nomusic.place_forget()
                    self.mlist.insert(END, "   ♪  {0}".format(s))
                    self.mlist.config()
Player(root).place()

root.mainloop()
