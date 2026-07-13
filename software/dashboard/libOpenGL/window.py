import glfw

class CallWindow():
    def __init__(self):

        self.window = None

    def build(self):
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

        if not glfw.init():
            raise RuntimeError("Não foi possível inicializar o GLFW")

        self.window = glfw.create_window(
            500, 500, "Visualizer", None, None
        )

        if not self.window:
            glfw.terminate()
            raise RuntimeError("Não foi possível criar a janela")

        glfw.make_context_current(self.window)

    def __close(self):

        glfw.terminate()

    
    def loop(self):

        if self.window is None:
            raise RuntimeError("A janela ainda não foi criada.")

        while not glfw.window_should_close(self.window):
            glfw.poll_events()
            glfw.swap_buffers(self.window)

        self.__close()


if __name__ == "__main__":

    call = CallWindow()
    call.build()
    call.loop()