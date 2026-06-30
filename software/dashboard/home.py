import tkinter as tk
import os
import json
from pathlib import Path
from tkinter import ttk
from windows.newproject import NewProject
from source.Astro_ConfigManager import ConfigManager

class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard")
        self.geometry("800x600")
        self.frame = None
    
        self.path_projects = os.path.join(os.getcwd(), "./software/data")
        self.config = ConfigManager()

        self.load_projects()
        self.create_widgets()
        

    def clear(self):
        if self.frame:
            self.frame.destroy()

    def load_projects(self):
        self.load = Path(self.path_projects)
    
    def new_project(self):
        NewProject(self)


    def showConfig(self):
        self.clear()
        self.frame = ttk.Frame(self)
        self.frame_Bg = tk.Frame(self.frame, bg=self.config.json_tema["bg-CorPrincipal"])
        self.frame_tema = tk.Frame(self.frame_Bg, bg=self.config.json_tema["bg-CorPrincipal"], width=200, height=30)

        self.frame.pack(fill="both", expand=True)   
        self.frame_Bg.pack(fill="both", expand=True)  
        self.frame_tema.pack(side=tk.RIGHT, padx=10, pady=10) 
        self.frame_tema.pack_propagate(False)

        self.botton_undo = tk.Button(
            self.frame_Bg, text="Home", 
            command=self.create_widgets,
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

        self.create_widgets()

    
    def create_widgets(self):
        self.clear()
        self.frame = ttk.Frame(self)
        self.frame.pack(fill="both", expand=True)

        
        self.container = tk.Frame(self.frame, bg=self.config.json_tema["bg-CorPrincipal"])
        self.container.pack(fill=tk.BOTH, expand=True)

        self.frame_aside = tk.Frame(self.container, bg=self.config.json_tema["bg-CorSecundaria"], width=200)
        self.frame_aside.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        self.frame_aside.pack_propagate(False)

        self.frame_body = tk.Frame(self.container, bg=self.config.json_tema["bg-CorSecundaria"])
        self.frame_body.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.frame_menu = tk.Frame(self.frame_aside, bg=self.config.json_tema["bg-CorSecundaria"], height=50)
        self.frame_menu.pack(side=tk.BOTTOM, fill=tk.X, padx=0, pady=50)

        self.create_dashboardFolder()

        self.style_textTitle = ttk.Style()
        self.style_textTitle.configure("Titulo.TLabel", foreground="#388eff", background = self.config.json_tema["bg-CorSecundaria"])

        # Add a label to the dashboard.aside
        self.label = ttk.Label(
            self.frame_aside,
            text="Projeto Astro",
            font=("Helvetica", 18),
            style="Titulo.TLabel"
        )
        self.label.pack(anchor=tk.NW, padx=20, pady=20)

        # Add buttons to the dashboard.aside.menu
        self.button_newProject = tk.Button(
            self.frame_menu,
            text="New Project",
            command=self.new_project,
            foreground= self.config.json_tema["font-geral"],
            width=50,
            background=self.config.json_tema["botton"]
        )
        self.button_newProject.pack(anchor=tk.W, padx=20, pady=20)

        self.button_settings = tk.Button(
            self.frame_menu,
            text="Settings",
            command=self.showConfig,
            foreground= self.config.json_tema["font-geral"],
            width=50,
            background= self.config.json_tema["botton"]
        )
        self.button_settings.pack(anchor=tk.W, padx=20, pady=20)

        self.button_exit = tk.Button(
            self.frame_menu,
            text="Exit",
            command=self.quit,
            foreground= self.config.json_tema["font-geral"],
            width=50,
            background= self.config.json_tema["botton"]
        )
        self.button_exit.pack(anchor=tk.W, padx=20, pady=20)

    def create_dashboardFolder(self):
        for widget in self.frame_body.winfo_children():
            widget.destroy()

        self.load_projects()

        for project in self.load.iterdir():
            if project.is_dir():
                button = tk.Button(
                    self.frame_body,
                    text=project.name,
                    foreground= self.config.json_tema["font-geral"],
                    width=50,
                    background=self.config.json_tema["botton"]
                )
                button.pack(fill=tk.X, padx=10, pady=5)
            

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()