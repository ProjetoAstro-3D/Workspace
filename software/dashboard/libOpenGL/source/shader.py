import glm
import os
from OpenGL.GL import *
import OpenGL.GL.shaders as gls

class Shader:

    def __init__(self, vertex_name, fragment_name):

        # Caminho da pasta libOpenGL
        root = os.path.dirname(os.path.dirname(__file__))

        # Caminho da pasta shaders
        shaders_path = os.path.join(root, "shaders")

        self.path_vertex = os.path.join(shaders_path, vertex_name)
        self.path_fragment = os.path.join(shaders_path, fragment_name)

        print("Vertex:", self.path_vertex)
        print("Fragment:", self.path_fragment)

        self.vertex = self.sourceVS()
        self.fragment = self.sourceFS()
        
        self.program = self.__build()

    def sourceFS(self):
        with open(self.path_fragment, "r", encoding="utf-8") as file:
            return file.read()

    def sourceVS(self):
        with open(self.path_vertex, "r", encoding="utf-8") as file:
            return file.read()
        
    def __build(self):
        self.id_vertexS = gls.compileShader(self.vertex, GL_VERTEX_SHADER)
        self.id_fragmentS = gls.compileShader(self.fragment, GL_FRAGMENT_SHADER)
        
        return gls.compileProgram(self.id_vertexS, self.id_fragmentS)
    
    def use(self):
        glUseProgram(self.program)

    def set_mat4(self, name, matrix):
        location = glGetUniformLocation(self.program, name)

        glUniformMatrix4fv(
            location,
            1,
            GL_FALSE,
            glm.value_ptr(matrix)
        )