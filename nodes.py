import tkinter as tk

class Button:
    def __init__(self, cmd, txt, row, col, parent):
        btn = tk.Button(parent, text=txt, command=cmd)
        btn.grid(row=row, column=col)

class Label:
    def __init__(self, text, row, col, colspan, parent):
        self.row = row
        self.col = col
        self.colspan = colspan
        self.parent = parent
        self.lbl = tk.Label(parent, text=text)
        self.lbl.grid(row=row, column=col, columnspan=colspan)

    def configure(self, text):
        self.lbl.config(text=text)

class Entry:
    def __init__(self, parent, var, row, col):
        self.var = var
        ent = tk.Entry(parent, textvariable=var)
        ent.grid(row=row, column=col)

    def get(self):
        return self.var.get()