import os
import json

class ConfigManager:
    def __init__(self):

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

        self.config_dir = os.path.join(os.getcwd(), "./software/dashboard/config")
        self.config = None
        self.json_tema = None

        #Metodos:

        self.__load()

    def __load(self):
        with open(f"{self.config_dir}/default.json", "r") as read:
            
            self.config = json.load(read)
            self.json_tema = self.config["color"]["Tema"][self.config["geral"]["Tema"]]

    def set_tema(self, tema):
        
        lastConfig = self.config

        if lastConfig["geral"]["Tema"] == tema:
            return 0
        
        with open(f"{self.config_dir}/default.json", "w") as file:
            if lastConfig["geral"]["Tema"] != tema and lastConfig["geral"]["Tema"] == "light":   
                lastConfig["geral"]["Tema"] = "dark"
                json.dump(lastConfig, file, indent=4)

            if lastConfig["geral"]["Tema"] != tema and lastConfig["geral"]["Tema"] == "dark":   
                lastConfig["geral"]["Tema"] = "light"
                json.dump(lastConfig, file, indent=4)

        self.__load()