import os
import tkinter as tk
from tkinter import ttk
import subprocess as sp
import configparser as cfg
from . import menubar as menu
from tkinter import filedialog
from . import custom_style as cs

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master,width=1280,height=800)
        menubar=menu.Menubar(master, [self.add_tab, self.fileopen, self.filesave, self.filesaveas, self.run])
        master.title('Loophole')
        master.geometry('1280x800')
        self.config=cfg.ConfigParser()
        self.config.read('config.ini', encoding='utf-8')
        self.startupinfo = sp.STARTUPINFO()
        self.startupinfo.dwFlags |= sp.STARTF_USESHOWWINDOW
        self.notebook=cs.CustomNotebook(width=1050, height=600)
        self.notebook.pack(anchor=tk.NE)
        self.output_frame=tk.Frame(master,width=1050,height=200,bg='#606060')
        self.output_frame.pack(anchor=tk.NW,padx=(226,0),ipady=200,fill=tk.BOTH)
        self.op=tk.Label(self.output_frame,fg='white',background='#202020')
        self.op.pack(anchor=tk.NW,padx=(15,0),pady=15)
        self.tframes=[]
        self.fnames=[]

    def add_tab(self,fname):
        tframe=cs.SbTextFrame(self.notebook)
        self.tframes.append(tframe)
        if os.path.isfile(fname):
            try:
                with open(fname,'r', encoding='utf-8') as f:
                    lines=f.readlines()
            except:
                pass
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
        try:
            with open(fname,'w', encoding='utf-8') as f:
                f.writelines(tframe.text.get('1.0','end-1c'))
        except:
            pass

    def filesaveas(self):
        idx=self.notebook.tabs().index(self.notebook.select())
        fname=filedialog.asksaveasfilename()
        tframe=self.tframes[idx]
        try:
            with open(fname,'w', encoding='utf-8') as f:
                f.writelines(tframe.text.get('1.0','end-1c'))
        except:
            pass

    def run(self):
        self.filesave()
        idx=self.notebook.tabs().index(self.notebook.select())
        fname=self.fnames[idx]
        sp.run('{} {}'.format(self.config['DEFAULT']['csc_path'],fname),startupinfo=self.startupinfo)
        self.op['text']=sp.run([os.path.join(os.getcwd(),"{}.exe".format(os.path.splitext(fname)[0]))], check=True, shell=True, stdout=sp.PIPE, stderr=sp.PIPE ,encoding="utf-8",startupinfo=self.startupinfo).stdout

def main():
    root=tk.Tk()
    app=Application(root)
    root.mainloop()
