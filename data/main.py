import os
import inspect
import tkinter as tk
from tkinter import ttk
import subprocess as sp
from . import menubar as menu
from tkinter import filedialog
from . import custom_style as cs

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master,width=1280,height=800)
        menubar=menu.Menubar(master, [self.add_tab, self.fileopen, self.filesave, self.filesaveas, self.run])
        master.title('Loophole')
        master.geometry('1280x800')
        self.csc_path='C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\csc.exe'
        self.notebook=cs.CustomNotebook(width=1050, height=600)
        self.notebook.pack(anchor=tk.NE)
        self.output_frame=tk.Frame(master,width=1050,height=200,bg='black')
        self.output_frame.pack(padx=(225,0))
        self.op=tk.Label(self.output_frame,fg='white',text='OooooooooooooooooooooooK',background='#0000aa')
        self.op.pack(side=tk,LEFT)
        self.tframes=[]
        self.fnames=[]

    def add_tab(self,fname):
        tframe=cs.SbTextFrame(self.notebook)
        self.tframes.append(tframe)
        if os.path.isfile(fname):
            with open(fname,'r', encoding='utf-8') as f:
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
        with open(fname,'w', encoding='utf-8') as f:
            f.writelines(tframe.text.get('1.0','end-1c'))

    def filesaveas(self):
        idx=self.notebook.tabs().index(self.notebook.select())
        fname=filedialog.asksaveasfilename()
        tframe=self.tframes[idx]
        with open(fname,'w', encoding='utf-8') as f:
            f.writelines(tframe.text.get('1.0','end-1c'))

    def run(self):
        idx=self.notebook.tabs().index(self.notebook.select())
        fname=self.fnames[idx]
        sp.run('{} {}'.format(self.csc_path,fname))
        self.op['text']=sp.run([os.path.join(os.getcwd(),"{}.exe".format(os.path.splitext(fname)[0]))], check=True, shell=True, stdout=sp.PIPE, stderr=sp.PIPE ,encoding="utf-8")

def main():
    root=tk.Tk()
    app=Application(root)
    root.mainloop()
