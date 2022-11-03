import tkinter as tk
from functools import partial

class Menubar(tk.Menu):
    def __init__(self, master, commands):
        super().__init__(master)
        master.config(menu=self)
        self.commands=commands
        self.file_menu()

    def cm_func(self, n, event=None, text=None):
        if text==None:
            self.commands[n]()
        else:
            self.commands[n](text)

    def file_menu(self):
        file_menu=tk.Menu(self, tearoff=0)
        file_menu.add_command(label='New', command=lambda:self.cm_func(0,text='     untitled     '))
        file_menu.add_command(label='Open', command=lambda:self.cm_func(1))
        file_menu.add_command(label='Save', command=lambda:self.cm_func(2))
        file_menu.add_command(label='Save As', command=lambda:self.cm_func(3))
        self.add_cascade(label="File", menu=file_menu)
        self.bind_all('<Control-Shift-S>', partial(self.cm_func, 3))
        self.bind_all('<Alt-r>', partial(self.cm_func, 4))
