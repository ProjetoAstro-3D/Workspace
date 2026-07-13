import os
import json


class ConfigManager:
    def __init__(self, project):

        """
            Gerencia as configurações globais do software.

            Responsável por carregar, armazenar e fornecer acesso às configurações
            presentes no diretório de configuração. Ao ser instanciada, a classe
            realiza automaticamente a leitura do arquivo de configuração padrão e
            disponibiliza seus dados através de seus atributos.

            Atributos:
                config_dir (str): Caminho para o diretório de configurações.
                config (dict): Conteúdo completo do arquivo de configuração.
                json_tema (dict): Configuração do tema atualmente selecionado.
        """

        #Variaveis:

        self.project = project

        self.config_defaltDir = os.path.join(os.getcwd(), "./software/dashboard/config")
        self.config_projDir = self.__source_proj()
        self.config = None
        self.json_tema = None

        #Metodos:

        self.__load()

    def __source_proj(self):
        if not self.project:
            return None

        return os.path.join(os.getcwd(), f"./software/data/{self.project}")

    def __load(self):
        with open(f"{self.config_defaltDir}/default.json", "r") as read:
            
            self.config = json.load(read)
            self.json_tema = self.config["color"]["Tema"][self.config["geral"]["Tema"]]
        if self.config_projDir != None:
            self.config_projDir = self.__source_proj()
            with open(f"{self.config_projDir}/config.json", "r") as read:
                self.config_proj = json.load(read)

    def set_tema(self, tema):
        
        lastConfig = self.config

        if lastConfig["geral"]["Tema"] == tema:
            return 0
        
        with open(f"{self.config_defaltDir}/default.json", "w") as file:
            if lastConfig["geral"]["Tema"] != tema and lastConfig["geral"]["Tema"] == "light":   
                lastConfig["geral"]["Tema"] = "dark"
                json.dump(lastConfig, file, indent=4)

            if lastConfig["geral"]["Tema"] != tema and lastConfig["geral"]["Tema"] == "dark":   
                lastConfig["geral"]["Tema"] = "light"
                json.dump(lastConfig, file, indent=4)
        
        self.__load()

    def set_name(self, name):
        if self.config_projDir != None:
            lastConfig = self.config_proj

            if lastConfig["project_name"] == name:
                return 0
            
            with open(f"{self.config_projDir}/config.json", "w") as file:
                
                lastConfig["project_name"] = name
                json.dump(lastConfig, file, indent=4)

            os.rename(f"./software/data/{self.project}", f"./software/data/{name}")
            self.project = name
            self.__load()
