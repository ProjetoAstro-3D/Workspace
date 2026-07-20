import re
import tkinter as tk
from typing import Literal
from tkinter import ttk
from dashboard.libTkinterPy.source.Astro_Builder import AstroBuilder
from dashboard.libTkinterPy.source.Astro_ConfigManager import ConfigManager

def validate(text: str) -> bool:
    return text == "" or all(c.isalnum() or c in " -" for c in text)

class NewProject(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
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
        

        vcmd = (self.register(self.validate_number), "%P")
        vcm = (self.register(validate), "%P")
        frame_leftSide = tk.Frame(self)
        frame_leftSide.pack(side=tk.LEFT, fill=tk.Y)

        label_name = ttk.Label(frame_leftSide, text="Project Name:").pack(anchor=tk.W,pady=10, padx = 10)
        self.entry_name = ttk.Entry(frame_leftSide, width= 40, validate="key",validatecommand=vcm)
        self.entry_name.pack(anchor=tk.W,pady=5, padx = 10)

        label_description = ttk.Label(frame_leftSide, text="Project Description:").pack(anchor=tk.W,pady=10, padx = 10)
        self.entry_description = tk.Text(frame_leftSide, height=10, width=30)
        self.entry_description.pack(anchor=tk.W,pady=5, padx = 10)


        frame_rightSide = tk.Frame(self)
        frame_rightSide.pack(fill=tk.BOTH, expand=True)
        #Options:

        material_list = ["PLA", "PETG", "ABS", "TPU"]
        filamentDiameter_list = [1.75, 2.85]
        quality = ["High", "Medium", "Low"]

        # Variable to keep track of the option
        # selected in OptionMenu
        self.value_insideMaterial = tk.StringVar(frame_rightSide)
        self.value_insideFilamentD = tk.StringVar(frame_rightSide)
        self.value_insideQuality = tk.StringVar(frame_rightSide)

        # Set the default value of the variable
        self.value_insideMaterial.set("Select an Option")
        self.value_insideFilamentD.set("Select an Option")
        self.value_insideQuality.set("Select an Option")


        #__________________________________________________________________________________________________
        

        label_material = ttk.Label(frame_rightSide, text="Material:").pack(anchor=tk.W,pady=10, padx = 10)
        self.entry_material = tk.OptionMenu(frame_rightSide, self.value_insideMaterial, *material_list)
        self.entry_material.pack(anchor=tk.W,pady=5, padx = 10)

        label_filament_diameter = ttk.Label(frame_rightSide, text="Filament Diameter (mm):").pack(anchor=tk.W,pady=10, padx = 10)
        self.entry_filament_diameter = tk.OptionMenu(frame_rightSide, self.value_insideFilamentD, *filamentDiameter_list)
        self.entry_filament_diameter.pack(anchor=tk.W,pady=5, padx = 10)

        label_quality = ttk.Label(frame_rightSide, text="Quality:").pack(anchor=tk.W,pady=10, padx = 10)
        self.entry_quality = tk.OptionMenu(frame_rightSide, self.value_insideQuality, *quality)
        self.entry_quality.pack(anchor=tk.W,pady=5, padx = 10)

        label_infill = ttk.Label(frame_rightSide, text="Infill (%):").pack(anchor=tk.W,pady=10, padx = 10)
        self.entry_infill = ttk.Entry(frame_rightSide, validate="key",validatecommand=vcmd)
        self.entry_infill.pack(anchor=tk.W,pady=5, padx = 10)

        button_newProjetc = tk.Button(self, text="New Project", command=self.create_project).pack(anchor=tk.CENTER, pady= 10, side=tk.BOTTOM)

    def create_project(self):
        project = AstroBuilder(
            project_name=self.entry_name.get(),
            project_description=self.entry_description.get("1.0", tk.END).strip(),
            material=self.value_insideMaterial.get(),
            filament_diameter=float(self.value_insideFilamentD.get()),
            quality=self.value_insideQuality.get(),
            infill=float(self.entry_infill.get())
        )

        project.init_builder()

        self.parent.create_dashboardFolder()

        self.destroy()
        

class Alterar(tk.Toplevel):
    def __init__(self, parent, controller,condicional: Literal["name"], name):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller
        self.name = name
        self.resizable(False, False)
        self.configManager = ConfigManager(name)

        self.condicional = condicional
    def save_name(self):
        arrg = self.input.get()
        self.configManager.set_name(arrg)
        self.controller.PainelConfig.show(arrg)
        self.destroy()

    def altName(self):
        vcmd = (self.register(validate), "%P")
        self.title("Alterar nome")
        self.geometry("400x200")
        self.label = tk.Label(
            self,
            text="Novo nome:"
        )
        self.input = tk.Entry(
            self,
            width= 30,
            validate="key",
            validatecommand=vcmd
        )
        self.button = tk.Button(
            self,
            text="Salvar",
            width=10,
            command = self.save_name
        )
        self.label.pack(
            side='left', 
            anchor="center",
            padx=2
            )
        self.input.pack(
            side='left', 
            anchor="center",
            padx=2
            )
        self.button.pack(
            side='left', 
            anchor="center",
            padx=5
            )

    def make(self):
        if self.condicional == "name":
            self.altName()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    new_project_window = Alterar(root, 'name')
    new_project_window.mainloop()