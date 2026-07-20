import glfw
import glm
from OpenGL.GL import *
from dashboard.libOpenGL.source.object import Object3D
from dashboard.libOpenGL.source.shader import Shader
from dashboard.libOpenGL.source.render import Renderer
from dashboard.libOpenGL.source.cam import Camera as Cam
from dashboard.libOpenGL.source.cameraControler import Cam_Controler
from dashboard.libOpenGL.source.ObjModel3D import Obj3D
from dashboard.libOpenGL.source.readerObj3D import STLreader
from dashboard.libOpenGL.primitives.bed import Plane
from dashboard.libOpenGL.primitives.grid import Grid
from dashboard.libOpenGL.widget.ButtonObj import Button


class CallWindow():
    def __init__(self, queue_TK_OG, queue_OG_TK):

        self.window = None
        self.queue_TK_OG = queue_TK_OG
        self.queue_OG_TK = queue_OG_TK
        self.msg = None
        
                
        
    def build(self):
        if not glfw.init():
            raise RuntimeError("Não foi possível inicializar o GLFW")
        
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

        self.monitors = glfw.get_monitors()

        if len(self.monitors) > 1:
            self.second_monitor = self.monitors[1]
        else:
            self.second_monitor = None
        
        if self.second_monitor is not None:
            glfw.window_hint(glfw.DECORATED, glfw.FALSE)
            x, y = glfw.get_monitor_pos(self.second_monitor)
            self.mode = glfw.get_video_mode(self.second_monitor)

            self.window = glfw.create_window(
                self.mode.size.width,
                self.mode.size.height,
                "Visualizer",
                None,  # Fullscreen no segundo monitor
                None
            )
            glfw.set_window_pos(self.window, x, y)
        else:
            self.window = glfw.create_window(
                800,
                600,
                "Visualizer",
                None,
                None
            )

        if not self.window:
            glfw.terminate()
            raise RuntimeError("Não foi possível criar a janela")

        glfw.make_context_current(self.window)
        glEnable(GL_DEPTH_TEST)
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
        self.shader_grid = self.grid_shader

        self.modelShader = Shader("default_Vshader.glsl", "default_Fshader.glsl")

        self.modelSTL = STLreader()
        self.modelSTL.load("C:\\Users\\henri\\OneDrive\\Desktop\\Rik2m6\\Workspace\\software\\data\\dev teste/craftModels/Models\\organizer.stl")

        self.ModelImport = Obj3D(self.modelShader, self.modelSTL, Renderer())

        self.cam = Cam()
        self.cam_controller = Cam_Controler(self.window, self.cam)
        glfw.set_cursor_pos_callback(
            self.window,
            self.cam_controller.cursor_callback
        )

        self.but = Button(
            [0.2,0.2],
            [-0.5,-0.5],
            "Teste"
        )
        self.but.set_widget()


    def verificar_queue(self):

        while not self.queue_TK_OG.empty():

            pass


    def __close(self):

        self.queue_OG_TK.put(
            {
                "cmd": "close_openGL"
            }
        )
        if self.window is not None:
            glfw.destroy_window(self.window)
            self.window = None

        glfw.terminate()

    
    def loop(self):

        if self.window is None:
            raise RuntimeError("A janela ainda não foi criada.")

        while not glfw.window_should_close(self.window):

            glfw.poll_events()

            self.cam_controller.process_input()
            glEnable(GL_SCISSOR_TEST)
            width, height = glfw.get_framebuffer_size(self.window)

            scene_width = int(width * 0.3)
            ui_width = width - scene_width

            glViewport(0, 0, scene_width, height)
            glScissor(0, 0, scene_width, height)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            # Bed
            self.shader_bed.use()
            self.shader_bed.set_mat4("model", self.cam.model)
            self.shader_bed.set_mat4("view", self.cam.view)
            self.shader_bed.set_mat4("projection", self.cam.projection)

            self.renderer_bed.draw(self.bed_obj)


            # Grid
            self.shader_grid.use()
            self.shader_grid.set_mat4("model", self.cam.model)
            self.shader_grid.set_mat4("view", self.cam.view)
            self.shader_grid.set_mat4("projection", self.cam.projection)

            self.renderer_grid.draw(self.grid_obj)

            #Model
            self.ModelImport.build(self.cam.model, self.cam.view, self.cam.projection)

          

            ui_width = width - scene_width

            glViewport(scene_width, 0, ui_width, height)
            glScissor(scene_width, 0, ui_width, height)

            glClearColor(0.2, 0.2, 0.2, 1)
            glClear(GL_COLOR_BUFFER_BIT)

            glDisable(GL_SCISSOR_TEST)
            glDisable(GL_DEPTH_TEST)
            ### TESTE ###

            self.but.render()

            glEnable(GL_DEPTH_TEST)

            #Queue .GET()

            self.verificar_queue()

            glfw.swap_buffers(self.window)

        self.__close()


if __name__ == "__main__":

    call = CallWindow()
    call.build()
    call.loop()