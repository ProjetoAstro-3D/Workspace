import numpy as np
from source.mesh import Mesh


class Plane:

    @staticmethod
    def create(width, depth):

        vertices = np.array([
            -width/2, 0.0, -depth/2,
            width/2, 0.0, -depth/2,
            width/2, 0.0,  depth/2,

            -width/2, 0.0, -depth/2,
            width/2, 0.0,  depth/2,
            -width/2, 0.0,  depth/2
        ], dtype=np.float32)

        return Mesh(vertices)