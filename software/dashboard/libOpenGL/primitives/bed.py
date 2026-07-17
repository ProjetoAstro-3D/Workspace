import numpy as np
from OpenGL.GL import *
from dashboard.libOpenGL.source.mesh import Mesh


class Plane:

    @staticmethod
    def create(width, depth):

        vertices = np.array([
            -width/2, 0.0, -depth/2,
            -width/2, 0.0,  depth/2,
            width/2, 0.0,  depth/2,
            width/2, 0.0, -depth/2,
        ], dtype=np.float32)
        indices = np.array(
            [
                [0, 1, 2],
                [0, 2, 3]
            ], dtype=np.uint32
        )

        return Mesh(vertices, indices, 3, GL_TRIANGLES)