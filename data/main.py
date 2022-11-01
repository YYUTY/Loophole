import os
import inspect
import tkinter as tk
from tkinter import ttk
from . import menubar as menu
from tkinter import filedialog
from . import custom_style as cs

class Application(tk.Frame):
    def __init__(self, master):
        menubar=menu.Menubar(master, [self.add_tab,self.fileopen,self.filesave])
        master.title('Loophole')
        master.geometry('640x480')
        self.notebook=cs.CustomNotebook(width=200, height=200)
        self.notebook.pack(fill='both',expand=1)
        self.tframes=[]
        self.fnames=[]

    def add_tab(self,fname):
        tframe=cs.SbTextFrame(self.notebook)
        self.tframes.append(tframe)
        if os.path.isfile(fname):
            with open(fname,'r') as f:
                lines=f.readlines()
            for line in lines:
                tframe.text.insert('end',line)
        self.fnames.append(fname)
        title=os.path.basename(fname)
        self.notebook.add(tframe,text=title)
        self.notebook.select(self.notebook.tabs()[self.notebook.index('end')-1])

    def fileopen(self):
        fname=filedialog.askopenfilename()
        self.add_tab(fname)

    def filesave(self):
        idx=self.notebook.tabs().index(self.notebook.select())
        fname=self.fnames[idx]
        tframe=self.tframes[idx]
        with open(fname,'w') as f:
            f.writelines(tframe.text.get('1.0','end-1c'))

def main():
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
