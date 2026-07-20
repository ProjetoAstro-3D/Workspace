import os
import json
class AstroBuilder:
        def __init__(
        self,
        project_name: str,
        project_description: str,
        material: str,
        filament_diameter: float,
        quality: str,
        infill: float
    ):
            self._project_name = project_name
            self._project_description = project_description
            self._material = material
            self._filament_diameter = filament_diameter
            self._quality = quality
            self._infill = infill
            self.__project_path = os.path.join(os.getcwd(), "./software/data", self._project_name)

        def build(self):
              os.makedirs(self.__project_path, mode=0o777, exist_ok=False)
              os.makedirs(os.path.join(self.__project_path, "craftModels"), mode=0o777, exist_ok=False)
              os.makedirs(os.path.join(f"{self.__project_path}/craftModels", "slices"), mode=0o777, exist_ok=False)
              os.makedirs(os.path.join(f"{self.__project_path}/craftModels", "Models"), mode=0o777, exist_ok=False)

        def save_project(self):
            project_config = {
                "project_name": self._project_name,
                "project_description": self._project_description,
                "material": self._material,
                "filament_diameter": self._filament_diameter,
                "quality": self._quality,
                "infill": self._infill
            }
            with open(os.path.join(self.__project_path, "config.json"), "w") as f:
                json.dump(project_config, f, indent=4)

        def init_builder(self):
            if self._filament_diameter not in [1.75, 2.85]:
                raise ValueError("Diâmetro de filamento inválido.")

            if self._quality not in ["High", "Medium", "Low"]:
                raise ValueError("Qualidade inválida.")

            if not (0 <= self._infill <= 100):
                raise ValueError("Infill deve estar entre 0 e 100.")

            self.build()
            self.save_project()

if __name__ == "__main__":
    builder = AstroBuilder(
        project_name="MyProject",
        project_description="This is a test project.",
        material="PLA",
        filament_diameter=1.75,
        quality="High",
        infill=20
    )
    builder.init_builder()