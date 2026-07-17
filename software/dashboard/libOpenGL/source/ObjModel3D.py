from dashboard.libOpenGL.source.object import Object3D
from dashboard.libOpenGL.source.mesh import Mesh
from OpenGL.GL import *
import glm

class Obj3D():
    def __init__(self, shader, STLreader, renderer):

        self.shader = shader
        self.STLreader = STLreader
        self.renderer = renderer
        self.mesh = Mesh(self.STLreader.vertices, self.STLreader.indices, 3, GL_TRIANGLES)
        self.mesh.normal(self.STLreader.normals)
        self.object = Object3D(self.mesh, self.shader)
        self.model_r = glm.mat4(1.0)
                # Escalar a peça
        self.model_r = glm.scale(
            self.model_r,
            glm.vec3(0.1, 0.1, 0.1)
        )
        self.model_r = glm.rotate(
            self.model_r,
            glm.radians(180),
            glm.vec3(1,0,0)
        )

        self.model_r = glm.translate(
            self.model_r,
            glm.vec3(0, -175, 0)
        )


        

    def build(self, model, view, projection):

        final_model = model * self.model_r

        self.shader.use()

        self.shader.set_mat4("model", self.model_r)
        self.shader.set_mat4("view", view)
        self.shader.set_mat4("projection", projection)

        self.renderer.draw(self.object)