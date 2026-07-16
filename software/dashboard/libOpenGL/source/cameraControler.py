import glfw

class Cam_Controler:

    def __init__(self, window, cam):
        self.window = window
        self.cam = cam

        self.rotating = False
        self.last_x = 0
        self.last_y = 0

        glfw.set_cursor_pos_callback(window, self.cursor_callback)
        glfw.set_mouse_button_callback(window, self.mouse_callback)


    def mouse_callback(self, window, button, action, mods):

        if button == glfw.MOUSE_BUTTON_LEFT:

            if action == glfw.PRESS:
                self.rotating = True

                x, y = glfw.get_cursor_pos(window)
                self.last_x = x
                self.last_y = y

            elif action == glfw.RELEASE:
                self.rotating = False


    def cursor_callback(self, window, xpos, ypos):

        if not self.rotating:
            return

        dx = xpos - self.last_x
        dy = ypos - self.last_y

        self.last_x = xpos
        self.last_y = ypos

        self.cam.rotate(dx, dy)

    def process_input(self):

        zoom_speed = 0.1

        if glfw.get_key(self.window, glfw.KEY_EQUAL) == glfw.PRESS:
            self.cam.zoom(-zoom_speed)

        if glfw.get_key(self.window, glfw.KEY_MINUS) == glfw.PRESS:
            self.cam.zoom(zoom_speed)