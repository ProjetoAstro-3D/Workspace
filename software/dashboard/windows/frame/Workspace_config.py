import os
import json
import tkinter as tk
from tkinter import ttk
from dashboard.windows.frame.newWindow import Alterar

class PainelConfig(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.__project_path = os.path.join(os.getcwd(), f"software/data/")
        self.json = None

    def AltName(self):
        var = Alterar(self.master,controller=self.controller, condicional="name", name = self.name)
        var.make()

    def create_widgets(self):
        filamentDiameter_list = [1.75, 2.85]
        quality = ["High", "Medium", "Low"]
        self.closeWS()
        frameName = tk.Frame(
            self.master,
            width=500,
            height=50
            )
        frameName.pack(
            side="top", 
            anchor="nw",
            expand= False
            )
        frameName.propagate(False)
        labelname = tk.Label(frameName, text=f"Nome do projeto: {self.json["project_name"]}")
        labelname.pack(side="top", anchor="w")
        bottonAlterarNome = tk.Button(
            frameName, 
            text="Alterar",
            command = self.AltName
            )
        bottonAlterarNome.pack(side="top", anchor="w")


        frameDesc = tk.Frame(
            self.master,
            width=500,
            height=20
            )
        frameDesc.pack(
            side="top", 
            anchor="nw",
            expand= False
            )
        frameDescOP = tk.Frame(
            self.master,
            width=500,
            height=50
            )
        frameDescOP.pack(
            side="top", 
            anchor="nw",
            expand= False
            )
        frameDesc.propagate(False)
        labelProjDesc = tk.Label(frameDesc, text = "Descrição:")
        textDesc = tk.Text(frameDescOP, width=40, height=4)
        labelProjDesc.pack(side="left", anchor="w")
        textDesc.pack(side="left", anchor="w", expand=False, fill = "none")
        textDesc.insert("1.0",self.json["project_description"])
        buttonDescSave = tk.Button(frameDescOP, text="alterar")
        buttonDescSave.pack(side="left", anchor="w")


        frameMaterial = tk.Frame(
            self.master,
            width=500,
            height=50
            )
        frameMaterial.pack(
            side="top", 
            anchor="nw",
            expand= False
            )
        frameMaterial.propagate(False)
        labelMat = tk.Label(frameMaterial, text="Material:")
        labelMat.pack(side="top", anchor="w")
        labelMatEsc = tk.Label(frameMaterial, text=self.json["material"])
        labelMatEsc.pack(side="top", anchor="w")


        frameFilamentDiameter = tk.Frame(
            self.master,
            width=500,
            height=50
            )
        frameFilamentDiameter.pack(
            side="top", 
            anchor="nw",
            expand= False
            )
        frameFilamentDiameter.propagate(False)
        self.value_insideFilamentD = tk.StringVar(frameFilamentDiameter)
        self.value_insideFilamentD.set(f"Atual escolha: {self.json["filament_diameter"]}")
        labelFilamentDiameter = tk.Label(frameFilamentDiameter, text = "Diametro do filamento:")
        self.entry_filament_diameter = tk.OptionMenu(frameFilamentDiameter, self.value_insideFilamentD, *filamentDiameter_list)
        labelFilamentDiameter.pack(side="top", anchor="w")
        self.entry_filament_diameter.pack(side="top", anchor="w")


        frameQuality = tk.Frame(
            self.master,
            width=500,
            height=50
            )
        frameQuality.pack(
            side="top", 
            anchor="nw",
            expand= False
            )
        labelQuality = tk.Label(frameQuality, text = "Qualidade da impressão:")
        labelQuality.pack(side="top", anchor="w")
        self.value_insideQuality = tk.StringVar(frameQuality)
        self.value_insideQuality.set(f"Qualidade Escolhida: {self.json["quality"]}")
        self.entry_filament_diameter = tk.OptionMenu(frameQuality, self.value_insideFilamentD, *filamentDiameter_list)
        self.entry_filament_diameter.pack(side="top", anchor="w")

        


    def show(self, name):
        self.name = name

        with open(f"{self.__project_path}/{name}/config.json", "r") as file:
            self.json = json.load(file)
        
        self.create_widgets()

   
    
    def closeWS(self):
        for widget in self.master.winfo_children():
            widget.destroy()