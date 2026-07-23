import tkinter as tk
import json
from pathlib import Path
from multiprocessing import Process, Queue

from dashboard.libTkinterPy.source.upload import UploadModel
from dashboard.libTkinterPy.source.Astro_ConfigManager import ConfigManager
from dashboard.libOpenGL.buildOpenGl import buildOpenGL



class PainelModels(tk.Frame):

    def __init__(self, master, controller, path):

        super().__init__(master)

        self.pathModels = f"{path}/craftModels/Models"
        self.path = path

        self.upModels = UploadModel()
        self.controller = controller

        self.queue_TK_OG = Queue()
        self.queue_OG_TK = Queue()

        self.config = ConfigManager(False)



    def runOpenGL(self):

        self.ButtonTableSlicerAcess.config(
            state=tk.DISABLED
        )


        self.process = Process(
            target=buildOpenGL,
            args=(
                self.queue_TK_OG,
                self.queue_OG_TK
            )
        )


        self.process.start()



    def active_button(self):

        self.ButtonTableSlicerAcess.config(
            state=tk.NORMAL
        )



    def Upload(self):

        arq = self.upModels.upload(
            self.pathModels
        )


        if not arq:
            return



        config_path = f"{self.path}/config.json"



        with open(config_path, "r") as file:
            jsonM = json.load(file)



        jsonM["ModelsPath"].append(arq)



        with open(config_path, "w") as file:
            json.dump(
                jsonM,
                file,
                indent=4
            )



        self.create_widgets()




    def create_widgets(self):

        self.closeWS()



        BG = self.config.json_tema["bg-CorSecundaria"]
        FG = self.config.json_tema["font-geral"]
        BTN = self.config.json_tema["botton"]



        ################################ LAYOUT #####################################


        self.layoutProj = tk.Frame(
            self.master,
            bg=BG
        )


        self.layoutProj.pack(
            side="left",
            anchor="nw",
            fill="x",
            expand=True
        )



        self.layoutTitlerModelProj = tk.Frame(
            self.layoutProj,
            bg=BG
        )


        self.layoutTitlerModelProj.pack(
            fill="x",
            side="top"
        )



        self.LayoutListModels = tk.Frame(
            self.layoutTitlerModelProj,
            bg=BG
        )


        self.LayoutListModels.pack(
            fill="x",
            side="bottom"
        )



        self.layoutTitlerSlicer = tk.Frame(
            self.layoutProj,
            bg=BG
        )


        self.layoutTitlerSlicer.pack(
            fill="x",
            side="top"
        )



        self.layoutBodySlicer = tk.Frame(
            self.layoutTitlerSlicer,
            bg=BG
        )


        self.layoutBodySlicer.pack(
            fill="x",
            side="bottom"
        )




        ################################ LABEL #####################################


        labelTitlerModelProj = tk.Label(
            self.layoutTitlerModelProj,
            text="MODELOS",
            bg=BG,
            fg=FG
        )


        labelTitlerModelProj.pack(
            side="left",
            padx=15
        )



        labelTitleSlice = tk.Label(
            self.layoutTitlerSlicer,
            text="SLICER [GCODE]",
            bg=BG,
            fg=FG
        )


        labelTitleSlice.pack(
            side="left",
            padx=15,
            pady=(50,0)
        )





        ################################ BUTTON #####################################


        ButtonUpload = tk.Button(
            self.layoutTitlerModelProj,
            text="Upload",
            command=self.Upload,
            bg=BTN,
            fg=FG,
            activebackground=BG,
            activeforeground=FG
        )


        ButtonUpload.pack(
            side="right",
            padx=15
        )




        self.ButtonTableSlicerAcess = tk.Button(
            self.layoutBodySlicer,
            text="[RENDER]",
            width=10,
            height=5,
            command=self.runOpenGL,
            bg=BTN,
            fg=FG,
            activebackground=BG,
            activeforeground=FG
        )


        self.ButtonTableSlicerAcess.pack(
            side="left",
            padx=15,
            pady=10
        )



        ################################ FUNÇÕES #####################################


        self.listModels()

        self.verificar_queue()





    def verificar_queue(self):

        while not self.queue_OG_TK.empty():

            msg = self.queue_OG_TK.get()


            if msg["cmd"] == "close_openGL":

                self.active_button()



        self.after(
            100,
            self.verificar_queue
        )





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
                    bg=self.config.json_tema["botton"],
                    fg=self.config.json_tema["font-geral"],
                    activebackground=self.config.json_tema["bg-CorSecundaria"],
                    activeforeground=self.config.json_tema["font-geral"]
                )


                button.pack(
                    fill=tk.X,
                    padx=10,
                    pady=5
                )





    def load_projects(self):

        self.load = Path(
            self.pathModels
        )




    def show(self):

        self.create_widgets()




    def closeWS(self):

        for widget in self.master.winfo_children():

            widget.destroy()