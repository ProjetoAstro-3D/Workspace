import os

class AstroBuilder:
        def __init__(
        self,
        project_name: str,
        project_description: str,
        material: str,
        filament_diameter: float,
        quality: str,
        layer_height: float,
        infill: float
    ):
            self._project_name = project_name
            self._project_description = project_description
            self._material = material
            self._filament_diameter = filament_diameter
            self._quality = quality
            self._layer_height = layer_height
            self._infill = infill
            self.__project_path = os.path.join(os.getcwd(), "workspace/software/data")

