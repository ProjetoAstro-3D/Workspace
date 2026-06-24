import tkinter as tk
from tkinter import ttk

class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        container = tk.Frame(self, bg="#d1d1d1")
        container.pack(fill=tk.BOTH, expand=True)

        frame_aside = tk.Frame(container, bg="#ebebeb", width=200)
        frame_aside.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        frame_aside.pack_propagate(False)

        frame_body = tk.Frame(container, bg="#ebebeb")
        frame_body.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        frame_menu = tk.Frame(frame_aside, bg="#ebebeb",height=50)
        frame_menu.pack(side=tk.BOTTOM, fill=tk.X, padx=0, pady=50)

        style_textTitle = ttk.Style()
        style_textTitle.configure("Titulo.TLabel", foreground="#388eff")

        # Add a label to the dashboard.aside
        label = ttk.Label(frame_aside, text="Projeto Astro", font=("Helvetica", 18), style="Titulo.TLabel").pack(anchor=tk.NW, padx=20, pady=20)
        # Add a button to the dashboard.aside.menu
        button_newProject = ttk.Button(frame_menu, text="New Project", padding=(20, 3)).pack(anchor=tk.W, padx=20, pady=20)
        button_openProject = ttk.Button(frame_menu, text="Open Project", padding=(20, 3)).pack(anchor=tk.W, padx=20, pady=20)
        button_settings = ttk.Button(frame_menu, text="Settings", padding=(20, 3)).pack(anchor=tk.W, padx=20, pady=20)
        button_exit = ttk.Button(frame_menu, text="Exit", command=self.quit, padding=(20, 3)).pack(anchor=tk.W, padx=20, pady=20)


if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()