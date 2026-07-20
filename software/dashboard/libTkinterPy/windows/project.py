import tkinter as tk
from tkinter import ttk
from dashboard.libTkinterPy.source.Astro_ConfigManager import ConfigManager
from dashboard.libTkinterPy.source.Astro_ReaderProjDir import ReaderDirP
from dashboard.libTkinterPy.windows.frame.Workspace_config import PainelConfig
from dashboard.libTkinterPy.windows.frame.Workspace_models import PainelModels
from dashboard.libTkinterPy.windows.frame.Workspace_run import PainelRun   

class ShowProjects(tk.Frame):
    def __init__(self, master, name, path):
        super().__init__(master)
        self.config = ConfigManager(None)
        self.nameProject = name
        self.txtDir = ReaderDirP(self.nameProject)
        self.style = ttk.Style()
        
        self.frames()
        self.PainelConfig = PainelConfig(self.frameWorkspace, self)
        self.PainelModels = PainelModels(self.frameWorkspace, self, path)
        self.PainelRun = PainelRun(self.frameWorkspace)

        self.style.theme_use("clam")
        self.style.configure(
            "Explorer.Treeview",
            background=self.config.json_tema["bg-CorSecundaria"],
            foreground=self.config.json_tema["font-geral"],
            fieldbackground=self.config.json_tema["bg-CorSecundaria"],
            borderwidth=0
        )

        self.style.map(
            "Explorer.Treeview",
            background=[("selected", "#388eff")],
            foreground=[("selected", "white")],
            fieldbackground=self.config.json_tema["bg-CorSecundaria"],
        )

        self.create_widget()

    def frames(self):

        self.frame = tk.Frame(
            self,
            bg = self.config.json_tema["bg-CorPrincipal"]
            )

        self.frameWorkspace = tk.Frame(
            self.frame,
            background = self.config.json_tema["bg-CorSecundaria"]
        )
        self.frame_tools = tk.Frame(
            self.frame,
            background = self.config.json_tema["bg-CorSecundaria"]
            )
        
        self.frameFolder = tk.Frame(
            self.frame,
            background = self.config.json_tema["bg-CorSecundaria"]
        )

        self.frame.pack(fill="both", expand=True)
        self.frameWorkspace.pack(
            side = "left"
        )
        self.frameFolder.pack(
            side = "left"
        )
        self.frameFolder.place(
            relheight = 0.75,
            relwidth = 0.22,
            relx=0.01, 
            rely=0.2
        )
        self.frameWorkspace.place(
            relheight = 0.75,
            relwidth = 0.75,
            relx=0.24, 
            rely=0.2
        )
        self.frame_tools.pack(
            side = "bottom"
            )
        self.frame_tools.place(
            relheight = 0.12,
            relwidth = 0.98,
            relx=0.01, 
            rely=0.07
        )

    def ToolsFunction(self):
        
        self.Btt_ConfigPainel = tk.Button(
            self.frame_tools,
            text = "Config",
            command = lambda: self.PainelConfig.show(self.nameProject)
            )
        self.Btt_ConfigPainel.pack(
            side = "right",
            anchor = "center",
            padx = 5
        )
        self.Btt_ModelsPainel = tk.Button(
            self.frame_tools,
            text = "models",
            command=self.PainelModels.show
        )
        self.Btt_ModelsPainel.pack(
            side = "right",
            anchor = "center",
            padx = 5
        )
        
        self.Btt_RunPainel= tk.Button(
            self.frame_tools,
            text = "run",
            command = self.PainelRun.show
        )
        self.Btt_RunPainel.pack(
            side = "right",
            anchor = "center",
            padx = 5
        )


    def asideDir(self):

        tree = ttk.Treeview(
            self.frameFolder,
            show="tree",
            style = "Explorer.Treeview"
        )

        tree.pack(
            fill="both",
            expand=True,
            anchor="w"
        )

        for var in self.txtDir.txtDir.iterdir():

            # Insere a pasta ou arquivo principal
            parent = tree.insert(
                "",
                "end",
                text=var.name,
                open=True
            )

            # Se for uma pasta, insere seus arquivos
            if var.is_dir():
                for item in var.iterdir():
                    tree.insert(
                        parent,
                        "end",
                        text=item.name
                    )


    def create_widget(self):

        self.botton_close = tk.Button(
            self.frame,
            text = "Close",
            foreground = self.config.json_tema["font-geral"],
            background = self.config.json_tema["botton"], 
            command = self.close
        )

        self.label_folder = tk.Label(
            self.frameFolder,
            text = f"Folder/{self.nameProject}",
            foreground = self.config.json_tema["font-geral"],
            background = self.config.json_tema["bg-CorSecundaria"]
        )

        self.botton_close.pack(
            anchor = tk.NW,
            side=tk.LEFT,
            pady = 5,
            padx = 5
        )

        self.label_folder.pack(
            anchor = "w",
            side = "top"
            )
        
        self.asideDir()
        self.PainelModels.show()
        self.ToolsFunction()
        
    def close(self):
        self.master.show_home()
