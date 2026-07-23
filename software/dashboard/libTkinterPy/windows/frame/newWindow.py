import tkinter as tk
from typing import Literal

from dashboard.libTkinterPy.source.Astro_Builder import AstroBuilder
from dashboard.libTkinterPy.source.Astro_ConfigManager import ConfigManager



def validate(text: str) -> bool:
    return text == "" or all(c.isalnum() or c in " -" for c in text)



class NewProject(tk.Toplevel):

    def __init__(self, parent):

        super().__init__(parent)

        self.parent = parent


        # =========================
        # CONFIG TEMA
        # =========================

        self.configManager = ConfigManager(False)

        self.BG = self.configManager.json_tema["bg-CorSecundaria"]
        self.FG = self.configManager.json_tema["font-geral"]
        self.BTN = self.configManager.json_tema["botton"]


        self.configure(
            bg=self.BG
        )


        self.title("New Project")
        self.geometry("600x500")
        self.resizable(False, False)


        self.create_widgets()



    def validate_number(self, value):

        if value == "":
            return True

        if not value.isdigit():
            return False

        return int(value) <= 100 and int(value) > 0



    def create_widgets(self):


        vcmd = (
            self.register(self.validate_number),
            "%P"
        )


        vcm = (
            self.register(validate),
            "%P"
        )



        # =========================
        # LADO ESQUERDO
        # =========================


        frame_leftSide = tk.Frame(
            self,
            bg=self.BG
        )


        frame_leftSide.pack(
            side=tk.LEFT,
            fill=tk.Y
        )



        tk.Label(
            frame_leftSide,
            text="Project Name:",
            bg=self.BG,
            fg=self.FG
        ).pack(
            anchor=tk.W,
            pady=10,
            padx=10
        )



        self.entry_name = tk.Entry(
            frame_leftSide,
            width=40,
            validate="key",
            validatecommand=vcm,
            bg=self.BG,
            fg=self.FG,
            insertbackground=self.FG
        )


        self.entry_name.pack(
            anchor=tk.W,
            pady=5,
            padx=10
        )



        tk.Label(
            frame_leftSide,
            text="Project Description:",
            bg=self.BG,
            fg=self.FG
        ).pack(
            anchor=tk.W,
            pady=10,
            padx=10
        )



        self.entry_description = tk.Text(
            frame_leftSide,
            height=10,
            width=30,
            bg=self.BG,
            fg=self.FG,
            insertbackground=self.FG
        )


        self.entry_description.pack(
            anchor=tk.W,
            pady=5,
            padx=10
        )





        # =========================
        # LADO DIREITO
        # =========================


        frame_rightSide = tk.Frame(
            self,
            bg=self.BG
        )


        frame_rightSide.pack(
            fill=tk.BOTH,
            expand=True
        )



        material_list = [
            "PLA",
            "PETG",
            "ABS",
            "TPU"
        ]


        filamentDiameter_list = [
            1.75,
            2.85
        ]


        quality = [
            "High",
            "Medium",
            "Low"
        ]



        self.value_insideMaterial = tk.StringVar(
            frame_rightSide
        )


        self.value_insideFilamentD = tk.StringVar(
            frame_rightSide
        )


        self.value_insideQuality = tk.StringVar(
            frame_rightSide
        )



        self.value_insideMaterial.set(
            "Select an Option"
        )


        self.value_insideFilamentD.set(
            "Select an Option"
        )


        self.value_insideQuality.set(
            "Select an Option"
        )




        # =========================
        # MATERIAL
        # =========================


        tk.Label(
            frame_rightSide,
            text="Material:",
            bg=self.BG,
            fg=self.FG
        ).pack(
            anchor=tk.W,
            pady=10,
            padx=10
        )



        self.entry_material = tk.OptionMenu(
            frame_rightSide,
            self.value_insideMaterial,
            *material_list
        )


        self.configure_optionmenu(
            self.entry_material
        )


        self.entry_material.pack(
            anchor=tk.W,
            pady=5,
            padx=10
        )





        # =========================
        # FILAMENTO
        # =========================


        tk.Label(
            frame_rightSide,
            text="Filament Diameter (mm):",
            bg=self.BG,
            fg=self.FG
        ).pack(
            anchor=tk.W,
            pady=10,
            padx=10
        )



        self.entry_filament_diameter = tk.OptionMenu(
            frame_rightSide,
            self.value_insideFilamentD,
            *filamentDiameter_list
        )


        self.configure_optionmenu(
            self.entry_filament_diameter
        )


        self.entry_filament_diameter.pack(
            anchor=tk.W,
            pady=5,
            padx=10
        )





        # =========================
        # QUALIDADE
        # =========================


        tk.Label(
            frame_rightSide,
            text="Quality:",
            bg=self.BG,
            fg=self.FG
        ).pack(
            anchor=tk.W,
            pady=10,
            padx=10
        )



        self.entry_quality = tk.OptionMenu(
            frame_rightSide,
            self.value_insideQuality,
            *quality
        )


        self.configure_optionmenu(
            self.entry_quality
        )


        self.entry_quality.pack(
            anchor=tk.W,
            pady=5,
            padx=10
        )





        # =========================
        # INFILL
        # =========================


        tk.Label(
            frame_rightSide,
            text="Infill (%):",
            bg=self.BG,
            fg=self.FG
        ).pack(
            anchor=tk.W,
            pady=10,
            padx=10
        )



        self.entry_infill = tk.Entry(
            frame_rightSide,
            validate="key",
            validatecommand=vcmd,
            bg=self.BG,
            fg=self.FG,
            insertbackground=self.FG
        )


        self.entry_infill.pack(
            anchor=tk.W,
            pady=5,
            padx=10
        )





        # =========================
        # BOTÃO
        # =========================


        tk.Button(
            self,
            text="New Project",
            command=self.create_project,
            bg=self.BTN,
            fg=self.FG,
            activebackground=self.BG,
            activeforeground=self.FG
        ).pack(
            anchor=tk.CENTER,
            pady=10,
            side=tk.BOTTOM
        )




    def configure_optionmenu(self, widget):

        widget.config(
            bg=self.BTN,
            fg=self.FG,
            activebackground=self.BG,
            activeforeground=self.FG
        )


        widget["menu"].config(
            bg=self.BG,
            fg=self.FG
        )





    def create_project(self):

        project = AstroBuilder(

            project_name=self.entry_name.get(),

            project_description=
            self.entry_description.get(
                "1.0",
                tk.END
            ).strip(),

            material=self.value_insideMaterial.get(),

            filament_diameter=
            float(
                self.value_insideFilamentD.get()
            ),

            quality=self.value_insideQuality.get(),

            infill=
            float(
                self.entry_infill.get()
            )
        )


        project.init_builder()


        self.parent.create_dashboardFolder()


        self.destroy()






class Alterar(tk.Toplevel):

    def __init__(
        self,
        parent,
        controller,
        condicional: Literal["name"],
        name
    ):

        super().__init__(parent)


        self.parent = parent
        self.controller = controller
        self.name = name


        self.resizable(
            False,
            False
        )


        self.configManager = ConfigManager(name)



        self.tema = ConfigManager(False)


        self.BG = self.tema.json_tema["bg-CorSecundaria"]
        self.FG = self.tema.json_tema["font-geral"]
        self.BTN = self.tema.json_tema["botton"]


        self.configure(
            bg=self.BG
        )


        self.condicional = condicional




    def save_name(self):

        arrg = self.input.get()


        self.configManager.set_name(
            arrg
        )


        self.controller.PainelConfig.show(
            arrg
        )


        self.destroy()




    def altName(self):


        vcmd = (
            self.register(validate),
            "%P"
        )


        self.title(
            "Alterar nome"
        )


        self.geometry(
            "400x200"
        )



        tk.Label(
            self,
            text="Novo nome:",
            bg=self.BG,
            fg=self.FG
        ).pack(
            side="left"
        )



        self.input = tk.Entry(
            self,
            width=30,
            validate="key",
            validatecommand=vcmd,
            bg=self.BG,
            fg=self.FG,
            insertbackground=self.FG
        )


        self.input.pack(
            side="left"
        )



        tk.Button(
            self,
            text="Salvar",
            width=10,
            command=self.save_name,
            bg=self.BTN,
            fg=self.FG,
            activebackground=self.BG,
            activeforeground=self.FG
        ).pack(
            side="left",
            padx=5
        )




    def make(self):

        if self.condicional == "name":
            self.altName()