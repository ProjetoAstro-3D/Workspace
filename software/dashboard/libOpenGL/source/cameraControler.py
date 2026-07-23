import glfw


class Cam_Controler:

    def __init__(self, window, cam):

        self.window = window
        self.cam = cam

        self.rotating = False

        self.last_x = 0.0
        self.last_y = 0.0

    # ==========================================
    # CALLBACK DO BOTÃO DO MOUSE
    # ==========================================

    def mouse_button_callback(self, window, button, action, mods):

        if button != glfw.MOUSE_BUTTON_LEFT:
            return

        if action == glfw.PRESS:

            self.rotating = True

            self.last_x, self.last_y = glfw.get_cursor_pos(window)

        elif action == glfw.RELEASE:

            self.rotating = False

    # ==========================================
    # CALLBACK DO MOVIMENTO DO MOUSE
    # ==========================================

    def cursor_callback(self, window, xpos, ypos):

        if not self.rotating:
            return

        dx = xpos - self.last_x
        dy = ypos - self.last_y

        self.last_x = xpos
        self.last_y = ypos

        self.cam.rotate(dx, dy)

    # ==========================================
    # TECLADO
    # ==========================================

    def process_input(self):

        zoom_speed = 0.3

        if glfw.get_key(self.window, glfw.KEY_EQUAL) == glfw.PRESS:
            self.cam.zoom(-zoom_speed)

        if glfw.get_key(self.window, glfw.KEY_MINUS) == glfw.PRESS:
            self.cam.zoom(zoom_speed)