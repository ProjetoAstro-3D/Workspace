import tkinter as tk
from tkinter import ttk

class PainelModels(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        

    def create_widgets(self):
        self.closeWS()
        labelteste = tk.Label(self.master, text="ModelsPainel")
        labelteste.pack()

    def show(self):
        self.create_widgets()
        
    def closeWS(self):
        for widget in self.master.winfo_children():
            widget.destroy()