import numpy as np
from OpenGL.GL import *
from dashboard.libOpenGL.source.mesh import Mesh

class Grid():

    @staticmethod
    def create(width, depth, divisions):

        vertices = []
        indices = []

        step_x = width / divisions
        step_z = depth / divisions

        half_width = width / 2
        half_depth = depth / 2

        vertex_index = 0

        # Linhas paralelas ao eixo X
        for i in range(1, divisions):
            z = -half_depth + i * step_z

            vertices.extend([
                -half_width, 1.0, z,
                 half_width, 1.0, z
            ])

            indices.extend([
                vertex_index,
                vertex_index + 1
            ])

            vertex_index += 2


        # Linhas paralelas ao eixo Z
        for i in range(1, divisions):
            x = -half_width + i * step_x

            vertices.extend([
                x, 1.0, -half_depth,
                x, 1.0, half_depth
            ])

            indices.extend([
                vertex_index,
                vertex_index + 1
            ])

            vertex_index += 2


        vertices = np.array(vertices, dtype=np.float32)
        indices = np.array(indices, dtype=np.uint32)

        return Mesh(vertices, indices, 3, GL_LINES)