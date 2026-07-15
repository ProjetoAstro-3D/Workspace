import glfw
import glm
from OpenGL.GL import *
from source.object import Object3D
from source.shader import Shader
from source.render import Renderer
from source.cam import Camera as Cam
from primitives.bed import Plane
from primitives.grid import Grid


class CallWindow():
    def __init__(self):

        self.window = None
        
        
    def build(self):
        if not glfw.init():
            raise RuntimeError("Não foi possível inicializar o GLFW")
        
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

        

        self.window = glfw.create_window(
            500, 500, "Visualizer", None, None
        )

        if not self.window:
            glfw.terminate()
            raise RuntimeError("Não foi possível criar a janela")

        glfw.make_context_current(self.window)
        glEnable(GL_DEPTH_TEST)
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        self.bed_mesh = Plane.create(200, 200)
        self.bed_shader = Shader("bed_Vshader.glsl", "bed_Fshader.glsl")
        self.bed_obj = Object3D(self.bed_mesh, self.bed_shader)
        self.renderer_bed = Renderer()
        self.shader_bed = self.bed_shader

        self.grid_mesh = Grid.create(200, 200, 10)
        self.grid_shader = Shader("grid_Vshader.glsl", "grid_Fshader.glsl")
        self.grid_obj = Object3D(self.grid_mesh, self.grid_shader)
        self.renderer_grid = Renderer()
        self.shader_grid = self.bed_shader

        self.shader_bed.use()

        self.cam = Cam()

    def __close(self):

        if self.window is not None:
            glfw.destroy_window(self.window)
            self.window = None

        glfw.terminate()

    
    def loop(self):

        if self.window is None:
            raise RuntimeError("A janela ainda não foi criada.")

        while not glfw.window_should_close(self.window):

            glfw.poll_events()

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
            self.shader_bed.set_mat4("model", self.cam.model)
            self.shader_bed.set_mat4("view", self.cam.view)
            self.shader_bed.set_mat4("projection", self.cam.projection)

            self.renderer_bed.draw(self.bed_obj)
            self.renderer_grid.draw(self.grid_obj)

            glfw.swap_buffers(self.window)

        self.__close()


if __name__ == "__main__":

    call = CallWindow()
    call.build()
    call.loop()