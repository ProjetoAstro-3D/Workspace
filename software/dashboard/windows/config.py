import tkinter as tk
from tkinter import ttk
from source.Astro_ConfigManager import ConfigManager

class ShowConfig(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config = ConfigManager(None)

        self.create_widgets()

    def create_widgets(self):
        self.frame = ttk.Frame(self)

        self.frame_Bg = tk.Frame(
            self.frame, 
            bg=self.config.json_tema["bg-CorPrincipal"])
        
        self.frame_tema = tk.Frame(
            self.frame_Bg, 
            bg=self.config.json_tema["bg-CorPrincipal"], 
            width=200, 
            height=30)

        self.frame.pack(fill="both", expand=True)   
        self.frame_Bg.pack(fill="both", expand=True)  
        self.frame_tema.pack(side=tk.RIGHT, padx=10, pady=10) 
        self.frame_tema.pack_propagate(False)

        self.botton_undo = tk.Button(
            self.frame_Bg, text="Home", 
            command=self.master.show_home,
            foreground= self.config.json_tema["font-geral"],
            background=self.config.json_tema["botton"]
            ).pack(anchor=tk.SW)
        
        #Option menu:
        #Opções
        list_Temas = ["light", "dark"]
        self.list_TemasDefault = tk.StringVar(self.frame_tema)
        self.list_TemasDefault.set(self.config.config["geral"]["Tema"])

        label_temaOp = tk.Label(
            self.frame_tema, text="Tema:", 
            bg=self.config.json_tema["bg-CorPrincipal"], 
            fg=self.config.json_tema["font-geral"])
        OpMenu_Tema = tk.OptionMenu(
            self.frame_tema, 
            self.list_TemasDefault, 
            *list_Temas)
        
        OpMenu_Tema.config(
            foreground= self.config.json_tema["font-geral"],
            background= self.config.json_tema["botton"]
        )

        label_temaOp.pack(anchor=tk.E, side=tk.LEFT)
        OpMenu_Tema.pack(anchor=tk.E, side=tk.LEFT, fill='both', expand=True)

        btn_saveConfig = tk.Button(
            self.frame_Bg, 
            text="Salvar Configurações", 
            command=self.btmSaveConfig,
            foreground= self.config.json_tema["font-geral"],
            background= self.config.json_tema["botton"])
        
        btn_saveConfig.pack(anchor="s")

    def btmSaveConfig(self):    

        self.config.set_tema(tema = self.list_TemasDefault.get())

        self.master.show_home()