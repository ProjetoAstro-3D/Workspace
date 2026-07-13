from OpenGL.GL import *
import ctypes

class Mess():
    def __init__(self, vertices, indices=None):

        self.vertices = vertices
        self.indices = indices

        self.id_vertexBufferObject = None
        self.vertexArrayOnject = None
        self.elementBufferObject = None

    def build_VBO(self):

        self.id_vertexBufferObject = glGenBuffers(1) #Criando o VBO

        glBindBuffer(GL_ARRAY_BUFFER, self.id_vertexBufferObject) #ativando o VBO

        glBufferData(  #Enviando os dados para o VBO
            GL_ARRAY_BUFFER, #Tipo de buffer
            self.vertices.nbytes, #Tamanho do buffer
            self.vertices,
            GL_STATIC_DRAW
        )


        glVertexAttribPointer( 
            0,          #codigo do atributo{posição}
            2,          #quantidade de valores do atributo
            GL_FLOAT,   #tipos dos valores do atributo 
            GL_FALSE,   #deseja normalizar os valores
            2*4,        #quantidade de bytes entre cada valores
            ctypes.c_void_p(0)
        )

        glEnableVertexAttribArray(0)