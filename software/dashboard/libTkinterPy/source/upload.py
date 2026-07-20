import os
import shutil
from tkinter import filedialog


class UploadModel:
    def __init__(self):
        self.title = "Selecione um arquivo"
        self.filetypes = [
            ("Arquivos STL", "*.stl")
        ]

    def upload(self, path):
        arquivo = filedialog.askopenfilename(
            title=self.title,
            filetypes=self.filetypes
        )

        if not arquivo:
            return None

        nome = os.path.basename(arquivo)
        nome_base, extensao = os.path.splitext(nome)

        destino = os.path.join(path, nome)

        contador = 1
        while os.path.exists(destino):
            novo_nome = f"{nome_base} ({contador}){extensao}"
            destino = os.path.join(path, novo_nome)
            contador += 1

        shutil.copy2(arquivo, destino)

        return destino    