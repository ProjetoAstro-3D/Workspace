import tkinter as tk
import json
from pathlib import Path
from dashboard.source.upload import UploadModel
from multiprocessing import Process, Queue
from dashboard.libOpenGL.buildOpenGl import buildOpenGL

class PainelModels(tk.Frame):
    def __init__(self, master, controller, path):
        super().__init__(master)
        self.pathModels = f"{path}/craftModels/Models"
        self.path = path
        self.upModels = UploadModel()
        self.controller = controller
        self.queue = Queue()

    def runOpenGL(self):
        print("1")
        self.process = Process(
            target = buildOpenGL,
            args = (self.queue,)
        )
        self.process.start()
        
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

        ################################ LAYOUT #####################################
       
        self.layoutProj = tk.Frame(self.master)
        self.layoutProj.pack(side="left", anchor="nw", fill="x", expand=True)

        self.layoutTitlerModelProj = tk.Frame(self.layoutProj)
        self.layoutTitlerModelProj.pack(fill="x", side="top")

        self.LayoutListModels = tk.Frame(self.layoutTitlerModelProj)
        self.LayoutListModels.pack(fill="x", side="bottom")

        self.layoutTitlerSlicer = tk.Frame(self.layoutProj)
        self.layoutTitlerSlicer.pack(fill="x", side="top")

        self.layoutBodySlicer = tk.Frame(self.layoutTitlerSlicer)
        self.layoutBodySlicer.pack(fill="x", side="bottom")


        ################################ LABEL #####################################

        labelTitlerModelProj = tk.Label(self.layoutTitlerModelProj, text = "MODELOS")
        labelTitlerModelProj.pack(side="left", padx = 15)

        labelTitleSlice = tk.Label(self.layoutTitlerSlicer, text="SLICER [GCODE]")
        labelTitleSlice.pack(side="left", padx = 15, pady = (50, 0))

        ################################ BUTTON #####################################

        ButtonUpload = tk.Button(self.layoutTitlerModelProj, text = "Upload", command= self.Upload)
        ButtonUpload.pack(side="right", padx = 15)

        ButtonTableSlicerAcess = tk.Button(self.layoutBodySlicer, text = "[RENDER]", width = 10, height = 5, command=self.runOpenGL)
        ButtonTableSlicerAcess.pack(side = "left", padx = 15, pady = 10)

        ################################ FUNÇÕES #####################################

        self.listModels()
        

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