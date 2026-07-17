from OpenGL.GL import *

class Renderer():
    def __init__(self):
        pass

    def draw(self, obj):

        obj.shader.use()

        glBindVertexArray(
            obj.mesh.id_vertexArrayObject
        )

        glDrawElements(
            obj.mesh.primitive,                   #Primitiva
            obj.mesh.comp * obj.mesh.indices_count,     #Quantidade de indices
            GL_UNSIGNED_INT,                #Tipo de indice
            None
        )

        glBindVertexArray(0)