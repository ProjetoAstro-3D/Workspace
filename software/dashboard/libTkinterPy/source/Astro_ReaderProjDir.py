from pathlib import Path
import os

class ReaderDirP:
    def __init__(self, name):
        self.name = name
        self.path = self.__path()
        self.txtDir = self.__reader()

    def __path(self):
        return os.path.join(os.getcwd(), f"./software/data/{self.name}")

    def __reader(self):
        return Path(self.path)