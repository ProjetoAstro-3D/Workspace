import tkinter as tk
from tkinter import ttk
from source.Astro_ConfigManager import ConfigManager

class ShowProjects(tk.Frame):
    def __init__(self, master, name):
        super().__init__(master)
        self.config = ConfigManager()
        self.nameProject = name

        self.create_widget()
    
    def frameFun(self):

        self.frame = tk.Frame(
            self,
            bg = self.config.json_tema["bg-CorPrincipal"]
            )
        self.frame.pack(fill="both", expand=True)

    def frameToolsFun(self):
        
        self.frame_tools = tk.Frame(
            self.frame,
            background = self.config.json_tema["bg-CorSecundaria"]
            )
        self.frame_tools.pack(
            side = "bottom"
            )
        self.frame_tools.place(
            relheight = 0.12,
            relwidth = 0.98,
            relx=0.01, 
            rely=0.07
        )

    def frameFolderDirFun(self):

        self.frameFolder = tk.Frame(
            self.frame,
            background = self.config.json_tema["bg-CorSecundaria"]
        )
        self.frameFolder.pack(
            side = "left"
        )
        self.frameFolder.place(
            relheight = 0.75,
            relwidth = 0.22,
            relx=0.01, 
            rely=0.2
        )

    def frameWorkspaceFun(self):

        self.frameWorkspace = tk.Frame(
            self.frame,
            background = self.config.json_tema["bg-CorSecundaria"]
        )
        self.frameWorkspace.pack(
            side = "left"
        )
        self.frameWorkspace.place(
            relheight = 0.75,
            relwidth = 0.75,
            relx=0.24, 
            rely=0.2
        )

    def create_widget(self):

        self.frameFun()
        self.frameToolsFun()
        self.frameFolderDirFun()
        self.frameWorkspaceFun()

        self.botton_close = tk.Button(
            self.frame,
            text = "Close",
            foreground = self.config.json_tema["font-geral"],
            background = self.config.json_tema["botton"], 
            command = self.close
        )

        self.label_NameProject = tk.Label(
            self.frame,
            text = self.nameProject,
            foreground = self.config.json_tema["font-geral"],
            background = self.config.json_tema["bg-CorPrincipal"]
        )

        self.botton_close.pack(
            anchor = tk.NW,
            side=tk.LEFT,
            pady = 5,
            padx = 5
        )
        self.label_NameProject.pack(
            anchor = tk.NW,
            side=tk.LEFT,
            pady = 5,
            padx = 5
        )

    def close(self):
        self.master.show_home()

