import tkinter as tk
import os
import json
from pathlib import Path
from tkinter import ttk
from windows.newproject import NewProject

class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard")
        self.geometry("800x600")
        self.frame = None

        self.path_projects = os.path.join(os.getcwd(), "./software/data")
        self.path_config = os.path.join(os.getcwd(), "./software/dashboard/config")
        self.load_projects()
        self.create_widgets()
        

    def clear(self):
        if self.frame:
            self.frame.destroy()

    def load_projects(self):
        self.load = Path(self.path_projects)
    
    def new_project(self):
        NewProject(self)

    def sourceConf(self) -> str: 
        with open(f"{self.path_config}/default.json", "r") as read:
            return json.load(read)


    def showConfig(self):
        self.clear()
        self.frame = ttk.Frame(self)
        self.frame.pack(fill="both", expand=True)   
        self.config_text = self.sourceConf()

        self.botton_undo = ttk.Button(self.frame, text="Home", command=self.create_widgets).pack(anchor=tk.SW)
        

    def create_widgets(self):
        self.clear()
        self.frame = ttk.Frame(self)
        self.frame.pack(fill="both", expand=True)

        
        self.container = tk.Frame(self.frame, bg="#d1d1d1")
        self.container.pack(fill=tk.BOTH, expand=True)

        self.frame_aside = tk.Frame(self.container, bg="#ebebeb", width=200)
        self.frame_aside.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        self.frame_aside.pack_propagate(False)

        self.frame_body = tk.Frame(self.container, bg="#ebebeb")
        self.frame_body.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.frame_menu = tk.Frame(self.frame_aside, bg="#ebebeb", height=50)
        self.frame_menu.pack(side=tk.BOTTOM, fill=tk.X, padx=0, pady=50)

        self.create_dashboardFolder()

        self.style_textTitle = ttk.Style()
        self.style_textTitle.configure("Titulo.TLabel", foreground="#388eff")

        # Add a label to the dashboard.aside
        self.label = ttk.Label(
            self.frame_aside,
            text="Projeto Astro",
            font=("Helvetica", 18),
            style="Titulo.TLabel"
        )
        self.label.pack(anchor=tk.NW, padx=20, pady=20)

        # Add buttons to the dashboard.aside.menu
        self.button_newProject = ttk.Button(
            self.frame_menu,
            text="New Project",
            padding=(20, 3),
            command=self.new_project
        )
        self.button_newProject.pack(anchor=tk.W, padx=20, pady=20)

        self.button_settings = ttk.Button(
            self.frame_menu,
            text="Settings",
            padding=(20, 3),
            command=self.showConfig
        )
        self.button_settings.pack(anchor=tk.W, padx=20, pady=20)

        self.button_exit = ttk.Button(
            self.frame_menu,
            text="Exit",
            command=self.quit,
            padding=(20, 3)
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
                    text=project.name
                )
                button.pack(fill=tk.X, padx=10, pady=5)
            

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()