import glm
import os
from OpenGL.GL import *
import OpenGL.GL.shaders as gls


class Shader:

    def __init__(self, vertex_name, fragment_name):

        root = os.path.dirname(os.path.dirname(__file__))

        shaders_path = os.path.join(
            root,
            "shaders"
        )

        self.path_vertex = os.path.join(
            shaders_path,
            vertex_name
        )

        self.path_fragment = os.path.join(
            shaders_path,
            fragment_name
        )

        self.vertex = self.sourceVS()
        self.fragment = self.sourceFS()

        self.program = self.__build()
        

    def sourceFS(self):

        with open(
            self.path_fragment,
            "r",
            encoding="utf-8"
        ) as file:
            return file.read()


    def sourceVS(self):

        with open(
            self.path_vertex,
            "r",
            encoding="utf-8"
        ) as file:
            return file.read()


    def __build(self):

        self.id_vertexS = gls.compileShader(
            self.vertex,
            GL_VERTEX_SHADER
        )

        self.id_fragmentS = gls.compileShader(
            self.fragment,
            GL_FRAGMENT_SHADER
        )


        program = glCreateProgram()

        glAttachShader(program, self.id_vertexS)
        glAttachShader(program, self.id_fragmentS)

        glLinkProgram(program)

        status = glGetProgramiv(program, GL_LINK_STATUS)

        return program


    def use(self):

        glUseProgram(
            self.program
        )


    def get_location(self, name):

        return glGetUniformLocation(
            self.program,
            name
        )


    # MATRIZ 4x4
    def set_mat4(self, name, matrix):

        location = self.get_location(name)

        glUniformMatrix4fv(
            location,
            1,
            GL_FALSE,
            glm.value_ptr(matrix)
        )


    # INT
    # usado para sampler2D
    def set_int(self, name, value):

        location = self.get_location(name)

        glUniform1i(
            location,
            value
        )


    # FLOAT
    def set_float(self, name, value):

        location = self.get_location(name)

        glUniform1f(
            location,
            value
        )


    # VEC2
    def set_vec2(self, name, x, y):

        location = self.get_location(name)
        glUniform2f(
            location,
            x,
            y
        )


    # VEC3
    def set_vec3(self, name, x, y, z):

        location = self.get_location(name)

        glUniform3f(
            location,
            x,
            y,
            z
        )