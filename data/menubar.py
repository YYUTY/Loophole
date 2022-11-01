import tkinter as tk

class Menubar(tk.Menu):
    def __init__(self, master, commands):
        super().__init__(master)
        master.config(menu=self)
        self.commands=commands
        self.file_menu()

    def file_menu(self):
        file_menu=tk.Menu(self, tearoff=0)
        file_menu.add_command(label='New', command=lambda:self.commands[0]('     untitled     '))
        file_menu.add_command(label='Open', command=lambda:self.commands[1]())
        file_menu.add_command(label='Save', command=lambda:self.commands[2]())
        file_menu.add_command(label='Save As')
        self.add_cascade(label="File", menu=file_menu)
