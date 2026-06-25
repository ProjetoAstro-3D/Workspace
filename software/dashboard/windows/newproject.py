import tkinter as tk
from tkinter import ttk

class NewProject(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("New Project")
        self.geometry("600x500")
        self.create_widgets()

    def create_widgets(self):
        label_name = ttk.Label(self, text="Project Name:").pack(anchor=tk.W,pady=10)
        self.entry_name = ttk.Entry(self).pack(anchor=tk.W,pady=5)

        label_description = ttk.Label(self, text="Project Description:").pack(anchor=tk.W,pady=10)
        self.entry_description = ttk.Entry(self).pack(anchor=tk.W,pady=5)

        label_material = ttk.Label(self, text="Material:").pack(anchor=tk.W,pady=10)
        self.entry_material = ttk.Entry(self).pack(anchor=tk.W,pady=5)

        label_filament_diameter = ttk.Label(self, text="Filament Diameter (mm):").pack(anchor=tk.W,pady=10)
        self.entry_filament_diameter = ttk.Entry(self).pack(anchor=tk.W,pady=5)

        label_quality = ttk.Label(self, text="Quality:").pack(anchor=tk.W,pady=10)
        self.entry_quality = ttk.Entry(self).pack(anchor=tk.W,pady=5)

        label_infill = ttk.Label(self, text="Infill (%):").pack(anchor=tk.W,pady=10)
        self.entry_infill = ttk.Entry(self).pack(anchor=tk.W,pady=5)
    

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    new_project_window = NewProject(root)
    new_project_window.mainloop()