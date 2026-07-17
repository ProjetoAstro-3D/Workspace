import os
import tkinter as tk
from tkinter import ttk
from pathlib import Path
from dashboard.windows.frame.newWindow import NewProject
from dashboard.source.Astro_ConfigManager import ConfigManager

class ShowHome(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.path_projects = os.path.join(os.getcwd(), "./software/data")
        self.config = ConfigManager(False)

        self.create_widgets()

    def create_widgets(self):
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
            command=self.master.show_config,
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
                    background=self.config.json_tema["botton"],
                    command=lambda name=project.name, path=project: self.master.show_project(name, path)
                )
                button.pack(fill=tk.X, padx=10, pady=5)
    
    def load_projects(self):
        self.load = Path(self.path_projects)
    
    def new_project(self):
        NewProject(self)