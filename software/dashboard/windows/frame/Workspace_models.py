import tkinter as tk
import json
from pathlib import Path
from source.upload import UploadModel
from tkinter import ttk

class PainelModels(tk.Frame):
    def __init__(self, master, controller, path):
        super().__init__(master)
        self.pathModels = f"{path}/craftModels/Models"
        self.path = path
        self.upModels = UploadModel()
        self.controller = controller
        
    def Upload(self):
        arq = self.upModels.upload(self.pathModels)

        if not arq:
            return

        config_path = f"{self.path}/config.json"

        # Ler o arquivo existente
        with open(config_path, "r") as file:
            jsonM = json.load(file)

        # Adicionar o novo modelo na lista
        jsonM["ModelsPath"].append(arq)

        # Salvar novamente
        with open(config_path, "w") as file:
            json.dump(jsonM, file, indent=4)

        for widget in self.layoutProj.winfo_children():
            widget.destroy()

        self.create_widgets()

    def create_widgets(self):
        self.closeWS()
       
        self.layoutProj = tk.Frame(self.master)
        self.layoutProj.pack(side="left", anchor="nw", fill="x", expand=True)
        self.layoutTitlerModelProj = tk.Frame(self.layoutProj)
        self.layoutTitlerModelProj.pack(fill="x", side="top")
        self.LayoutListModels = tk.Frame(self.layoutTitlerModelProj)
        self.LayoutListModels.pack(fill="x", side="bottom")

        self.listModels()

        labelTitlerModelProj = tk.Label(self.layoutTitlerModelProj, text = "Modelos")
        labelTitlerModelProj.pack(side="left", padx = 15)

        ButtonUpload = tk.Button(self.layoutTitlerModelProj, text = "Upload", command= self.Upload)
        ButtonUpload.pack(side="right", padx = 15)


    def listModels(self):
        for widget in self.LayoutListModels.winfo_children():
            widget.destroy()

        self.load_projects()

        for project in self.load.iterdir():
            if project.is_file():
                button = tk.Button(
                    self.LayoutListModels,
                    text=project.name,
                    width=50,
                )
                button.pack(fill=tk.X, padx=10, pady=5)
    
    def load_projects(self):
        self.load = Path(self.pathModels)
    

    def show(self):
        self.create_widgets()
        
    def closeWS(self):
        for widget in self.master.winfo_children():
            widget.destroy()