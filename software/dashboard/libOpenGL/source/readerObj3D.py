from pyassimp import load
import numpy as np

class STLreader():
    def __init__(self):

        self.mesh = None
        self.vertices = None
        self.indices = None
        self.normals = None
    
    def load(self, path):

        with load(path) as Object:

            if not Object.meshes:
                raise ValueError("O modelo não possui nenhuma malha.")
            
            self.mesh = Object.meshes[0]
            self.vertices = np.array(self.mesh.vertices, dtype = np.float32)
            self.indices = np.array(self.mesh.faces, dtype = np.uint32).flatten()
            self.normals = np.array(
                self.mesh.normals,
                dtype=np.float32
            )