from OpenGL.GL import *
import numpy as np
import ctypes


class TextMesh:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.vertices = np.array([
            # posição      UV
            0,      height, 0, 0,
            0,      0,      0, 1,
            width,  0,      1, 1,
            width,  height, 1, 0

        ], dtype=np.float32)


        self.indices = np.array([
            0, 1, 2,
            0, 2, 3
        ], dtype=np.uint32)


        self.vao = None
        self.vbo = None
        self.ebo = None

        self.build()


    def build(self):

        self.vao = glGenVertexArrays(1)
        self.vbo = glGenBuffers(1)
        self.ebo = glGenBuffers(1)


        glBindVertexArray(self.vao)


        # VBO
        glBindBuffer(
            GL_ARRAY_BUFFER,
            self.vbo
        )

        glBufferData(
            GL_ARRAY_BUFFER,
            self.vertices.nbytes,
            self.vertices,
            GL_STATIC_DRAW
        )


        # EBO
        glBindBuffer(
            GL_ELEMENT_ARRAY_BUFFER,
            self.ebo
        )

        glBufferData(
            GL_ELEMENT_ARRAY_BUFFER,
            self.indices.nbytes,
            self.indices,
            GL_STATIC_DRAW
        )


        stride = 4 * np.dtype(np.float32).itemsize


        # posição (x,y)
        glVertexAttribPointer(
            0,
            2,
            GL_FLOAT,
            GL_FALSE,
            stride,
            ctypes.c_void_p(0)
        )

        glEnableVertexAttribArray(0)



        # UV (u,v)
        glVertexAttribPointer(
            1,
            2,
            GL_FLOAT,
            GL_FALSE,
            stride,
            ctypes.c_void_p(
                2 * np.dtype(np.float32).itemsize
            )
        )

        glEnableVertexAttribArray(1)



        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)



    def draw(self):

        glBindVertexArray(self.vao)

        glDrawElements(
            GL_TRIANGLES,
            6,
            GL_UNSIGNED_INT,
            None
        )

        glBindVertexArray(0)