from OpenGL.GL import *
import numpy as np
import ctypes

class Mesh():
    def __init__(self, vertices, indices, num_componentes, primitive):

        self.comp = num_componentes
        self.vertices = vertices
        self.indices = indices
        self.primitive = primitive
        if self.primitive == GL_LINES and num_componentes > 2:
            self.comp = num_componentes - 1
        self.stride = num_componentes * np.dtype(np.float32).itemsize
        self.vertex_count = len(vertices)
        self.indices_count = len(indices)

        self.id_vertexBufferObject = None
        self.id_vertexArrayObject = None
        self.id_elementBufferObject = None

        self.build_VBO()

    def normal(self, normals):

        self.normals = normals
        self.normals_count = len(normals)

        glBindVertexArray(self.id_vertexArrayObject)

        self.normal_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.normal_vbo)

        glBufferData(
            GL_ARRAY_BUFFER,
            self.normals.nbytes,
            self.normals,
            GL_STATIC_DRAW
            )
        
        glVertexAttribPointer(
            1,
            3,
            GL_FLOAT,
            GL_FALSE,
            0,
            None
        )

        glEnableVertexAttribArray(1)
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

    def build_VBO(self):
        

        self.id_vertexArrayObject = glGenVertexArrays(1) #criando o VAO
        self.id_vertexBufferObject = glGenBuffers(1) #Criando o VBO
        self.id_elementBufferObject = glGenBuffers(1)

        glBindVertexArray(self.id_vertexArrayObject) #Ativando VAO
        glBindBuffer(GL_ARRAY_BUFFER, self.id_vertexBufferObject) #ativando o VBO
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.id_elementBufferObject) #ativando EBO

        glBufferData(  #Enviando os dados para o VBO
            GL_ARRAY_BUFFER, #Tipo de buffer
            self.vertices.nbytes, #Tamanho do buffer
            self.vertices,
            GL_STATIC_DRAW
        )

        glBufferData(                #Enviando os dados para o EBO
            GL_ELEMENT_ARRAY_BUFFER, #Tipo de buffer
            self.indices.nbytes,     #tamanho do buffer
            self.indices,            #indices
            GL_STATIC_DRAW,
        )

        glVertexAttribPointer( 
            0,                  #codigo do atributo{posição}
            3,                  #quantidade de valores do atributo
            GL_FLOAT,           #tipos dos valores do atributo 
            GL_FALSE,           #deseja normalizar os valores
            self.stride,        #quantidade de bytes entre cada valores
            ctypes.c_void_p(0)  #informando que é para começar no indice - 0
        )


        glEnableVertexAttribArray(0)
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)
