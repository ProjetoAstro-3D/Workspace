import glfw
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
from dashboard.libOpenGL.widget.drawWidgetInWidow import Draw_widget


class CallWindow:

    def __init__(self, queue_TK_OG, queue_OG_TK):

        self.window = None
        self.queue_TK_OG = queue_TK_OG
        self.queue_OG_TK = queue_OG_TK

    # ===========================
    # CALLBACKS
    # ===========================

    def cursor_callback(self, window, xpos, ypos):

        self.cam_controller.cursor_callback(
            window,
            xpos,
            ypos
        )

        self.widget_draw.cursor_callback(
            window,
            xpos,
            ypos
        )

    def mouse_button_callback(self, window, button, action, mods):

        self.cam_controller.mouse_button_callback(
            window,
            button,
            action,
            mods
        )

        self.widget_draw.mouse_button_callback(
            window,
            button,
            action,
            mods
        )

    # ===========================
    # BUILD
    # ===========================

    def build(self):

        if not glfw.init():
            raise RuntimeError("Não foi possível inicializar o GLFW")

        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

        monitors = glfw.get_monitors()

        if len(monitors) > 1:

            second_monitor = monitors[1]

            glfw.window_hint(glfw.DECORATED, glfw.FALSE)

            x, y = glfw.get_monitor_pos(second_monitor)
            self.mode = glfw.get_video_mode(second_monitor)

            self.window = glfw.create_window(
                self.mode.size.width,
                self.mode.size.height,
                "Visualizer",
                None,
                None
            )

            glfw.set_window_pos(self.window, x, y)

        else:

            self.mode = glfw.get_video_mode(monitors[0])
            glfw.window_hint(glfw.RESIZABLE, glfw.FALSE)

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

        # ----------------------------
        # BED
        # ----------------------------

        self.bed_mesh = Plane.create(200, 200)
        self.bed_shader = Shader(
            "bed_Vshader.glsl",
            "bed_Fshader.glsl"
        )

        self.bed_obj = Object3D(
            self.bed_mesh,
            self.bed_shader
        )

        self.renderer_bed = Renderer()

        # ----------------------------
        # GRID
        # ----------------------------

        self.grid_mesh = Grid.create(200, 200, 10)

        self.grid_shader = Shader(
            "grid_Vshader.glsl",
            "grid_Fshader.glsl"
        )

        self.grid_obj = Object3D(
            self.grid_mesh,
            self.grid_shader
        )

        self.renderer_grid = Renderer()

        # ----------------------------
        # STL
        # ----------------------------

        self.modelShader = Shader(
            "default_Vshader.glsl",
            "default_Fshader.glsl"
        )

        self.modelSTL = STLreader()

        self.modelSTL.load(
            self.queue_TK_OG.get()
        )

        self.ModelImport = Obj3D(
            self.modelShader,
            self.modelSTL,
            Renderer()
        )

        # ----------------------------
        # CAMERA
        # ----------------------------

        self.cam = Cam()

        self.cam_controller = Cam_Controler(
            self.window,
            self.cam
        )

        # ----------------------------
        # WIDGETS
        # ----------------------------
        fb_width, fb_height = glfw.get_framebuffer_size(self.window)

        scene_width = int(fb_width * 0.3)
        ui_width = fb_width - scene_width

        self.widget_draw = Draw_widget(
            window_size=[ui_width, fb_height],
            window_size_full=[fb_width, fb_height],
            window=self.window,
            viewport_offset=scene_width,
            obj3D=self.ModelImport
        )

        # ----------------------------
        # CALLBACKS GLFW
        # ----------------------------

        glfw.set_cursor_pos_callback(
            self.window,
            self.cursor_callback
        )

        glfw.set_mouse_button_callback(
            self.window,
            self.mouse_button_callback
        )

    # ===========================
    # QUEUE
    # ===========================

    def verificar_queue(self):

        while not self.queue_TK_OG.empty():
            pass

    # ===========================
    # CLOSE
    # ===========================

    def __close(self):

        self.queue_OG_TK.put(
            {
                "cmd": "close_openGL"
            }
        )

        if self.window:

            glfw.destroy_window(self.window)
            self.window = None

        glfw.terminate()

    # ===========================
    # LOOP
    # ===========================

    def loop(self):

        while not glfw.window_should_close(self.window):

            glfw.poll_events()

            self.cam_controller.process_input()

            width, height = glfw.get_framebuffer_size(self.window)

            scene_width = int(width * 0.3)
            
            ui_width = width - scene_width


            glEnable(GL_SCISSOR_TEST)

            # --------- CENA ---------

            glViewport(
                0,
                0,
                scene_width,
                height
            )

            glScissor(
                0,
                0,
                scene_width,
                height
            )

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            self.bed_shader.use()
            self.bed_shader.set_mat4("model", self.cam.model)
            self.bed_shader.set_mat4("view", self.cam.view)
            self.bed_shader.set_mat4("projection", self.cam.projection)

            self.renderer_bed.draw(self.bed_obj)

            self.grid_shader.use()
            self.grid_shader.set_mat4("model", self.cam.model)
            self.grid_shader.set_mat4("view", self.cam.view)
            self.grid_shader.set_mat4("projection", self.cam.projection)

            self.renderer_grid.draw(self.grid_obj)

            self.ModelImport.build(
                self.cam.model,
                self.cam.view,
                self.cam.projection
            )

            # --------- UI ---------

            glViewport(
                scene_width,
                0,
                ui_width,
                height
            )

            glScissor(
                scene_width,
                0,
                ui_width,
                height
            )

            glClearColor(0.2, 0.2, 0.2, 1.0)
            glClear(GL_COLOR_BUFFER_BIT)

            glDisable(GL_SCISSOR_TEST)
            glDisable(GL_DEPTH_TEST)

            self.widget_draw.draw()

            glEnable(GL_DEPTH_TEST)

            self.verificar_queue()

            glfw.swap_buffers(self.window)

        self.__close()


if __name__ == "__main__":

    call = CallWindow(None, None)
    call.build()
    call.loop()