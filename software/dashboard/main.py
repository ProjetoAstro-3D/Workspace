import tkinter as tk
from windows.config import ShowConfig
from windows.Home import ShowHome
from windows.project import ShowProjects

class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard")
        self.geometry("800x600")
  
        self.current_screen = None

        self.show_home()
        
    def change_screen(self, screen, *args, **kwargs):
        if self.current_screen:
            self.current_screen.destroy()

        self.current_screen = screen(self, *args, **kwargs)
        self.current_screen.pack(fill="both", expand=True)

    def show_home(self):
        self.change_screen(ShowHome)

    def show_config(self):
        self.change_screen(ShowConfig)

    def show_project(self, name, path):
        self.change_screen(ShowProjects, name, path)


if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()