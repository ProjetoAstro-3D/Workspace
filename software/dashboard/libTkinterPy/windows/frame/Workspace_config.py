import os
import json
import tkinter as tk

from dashboard.libTkinterPy.windows.frame.newWindow import Alterar
from dashboard.libTkinterPy.source.Astro_ConfigManager import ConfigManager


class PainelConfig(tk.Frame):

    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller
        self.__project_path = os.path.join(os.getcwd(), "software/data/")
        self.json = None

        self.config = ConfigManager(False)


    def AltName(self):

        var = Alterar(
            self.master,
            controller=self.controller,
            condicional="name",
            name=self.name
        )

        var.make()



    def create_widgets(self):

        filamentDiameter_list = [1.75, 2.85]
        quality = ["High", "Medium", "Low"]

        self.closeWS()


        BG = self.config.json_tema["bg-CorSecundaria"]
        FG = self.config.json_tema["font-geral"]
        BTN = self.config.json_tema["botton"]



        # =========================
        # NOME
        # =========================

        frameName = tk.Frame(
            self.master,
            width=500,
            height=50,
            bg=BG
        )

        frameName.pack(
            side="top",
            anchor="nw",
            expand=False
        )

        frameName.propagate(False)


        labelname = tk.Label(
            frameName,
            text=f"Nome do projeto: {self.json['project_name']}",
            bg=BG,
            fg=FG
        )

        labelname.pack(
            side="top",
            anchor="w"
        )


        bottonAlterarNome = tk.Button(
            frameName,
            text="Alterar",
            command=self.AltName,
            bg=BTN,
            fg=FG,
            activebackground=BG,
            activeforeground=FG
        )

        bottonAlterarNome.pack(
            side="top",
            anchor="w"
        )




        # =========================
        # DESCRIÇÃO
        # =========================


        frameDesc = tk.Frame(
            self.master,
            width=500,
            height=20,
            bg=BG
        )

        frameDesc.pack(
            side="top",
            anchor="nw",
            expand=False
        )


        frameDesc.propagate(False)


        labelProjDesc = tk.Label(
            frameDesc,
            text="Descrição:",
            bg=BG,
            fg=FG
        )


        labelProjDesc.pack(
            side="left",
            anchor="w"
        )



        frameDescOP = tk.Frame(
            self.master,
            width=500,
            height=100,
            bg=BG
        )


        frameDescOP.pack(
            side="top",
            anchor="nw",
            expand=False
        )



        textDesc = tk.Text(
            frameDescOP,
            width=40,
            height=4,
            bg=BG,
            fg=FG,
            insertbackground=FG
        )


        textDesc.insert(
            "1.0",
            self.json["project_description"]
        )


        textDesc.pack(
            side="left",
            anchor="w"
        )



        buttonDescSave = tk.Button(
            frameDescOP,
            text="Alterar",
            bg=BTN,
            fg=FG,
            activebackground=BG,
            activeforeground=FG
        )


        buttonDescSave.pack(
            side="left",
            anchor="w"
        )




        # =========================
        # MATERIAL
        # =========================


        frameMaterial = tk.Frame(
            self.master,
            width=500,
            height=50,
            bg=BG
        )


        frameMaterial.pack(
            side="top",
            anchor="nw",
            expand=False
        )


        frameMaterial.propagate(False)



        labelMat = tk.Label(
            frameMaterial,
            text="Material:",
            bg=BG,
            fg=FG
        )


        labelMat.pack(
            side="top",
            anchor="w"
        )



        labelMatEsc = tk.Label(
            frameMaterial,
            text=self.json["material"],
            bg=BG,
            fg=FG
        )


        labelMatEsc.pack(
            side="top",
            anchor="w"
        )




        # =========================
        # DIAMETRO FILAMENTO
        # =========================


        frameFilamentDiameter = tk.Frame(
            self.master,
            width=500,
            height=50,
            bg=BG
        )


        frameFilamentDiameter.pack(
            side="top",
            anchor="nw",
            expand=False
        )


        frameFilamentDiameter.propagate(False)



        labelFilamentDiameter = tk.Label(
            frameFilamentDiameter,
            text="Diâmetro do filamento:",
            bg=BG,
            fg=FG
        )


        labelFilamentDiameter.pack(
            side="top",
            anchor="w"
        )



        self.value_insideFilamentD = tk.StringVar(
            frameFilamentDiameter
        )


        self.value_insideFilamentD.set(
            str(self.json["filament_diameter"])
        )



        self.entry_filament_diameter = tk.OptionMenu(
            frameFilamentDiameter,
            self.value_insideFilamentD,
            *filamentDiameter_list
        )


        self.entry_filament_diameter.config(
            bg=BTN,
            fg=FG,
            activebackground=BG,
            activeforeground=FG
        )


        self.entry_filament_diameter["menu"].config(
            bg=BG,
            fg=FG
        )


        self.entry_filament_diameter.pack(
            side="top",
            anchor="w"
        )




        # =========================
        # QUALIDADE
        # =========================


        frameQuality = tk.Frame(
            self.master,
            width=500,
            height=50,
            bg=BG
        )


        frameQuality.pack(
            side="top",
            anchor="nw",
            expand=False
        )



        labelQuality = tk.Label(
            frameQuality,
            text="Qualidade da impressão:",
            bg=BG,
            fg=FG
        )


        labelQuality.pack(
            side="top",
            anchor="w"
        )



        self.value_insideQuality = tk.StringVar(
            frameQuality
        )


        self.value_insideQuality.set(
            self.json["quality"]
        )



        self.entry_quality = tk.OptionMenu(
            frameQuality,
            self.value_insideQuality,
            *quality
        )


        self.entry_quality.config(
            bg=BTN,
            fg=FG,
            activebackground=BG,
            activeforeground=FG
        )


        self.entry_quality["menu"].config(
            bg=BG,
            fg=FG
        )


        self.entry_quality.pack(
            side="top",
            anchor="w"
        )




    def show(self, name):

        self.name = name


        with open(
            f"{self.__project_path}/{name}/config.json",
            "r"
        ) as file:

            self.json = json.load(file)


        self.create_widgets()



    def closeWS(self):

        for widget in self.master.winfo_children():

            widget.destroy()