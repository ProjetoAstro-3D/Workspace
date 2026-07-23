import glfw
import numpy as np
from OpenGL.GL import *

from dashboard.libOpenGL.source.mesh import Mesh
from dashboard.libOpenGL.source.shader import Shader
from dashboard.libOpenGL.font.fontRender import FontRenderer
from dashboard.libOpenGL.source.object import Object3D
from dashboard.libOpenGL.font.meshFont import TextMesh
from dashboard.libOpenGL.source.render import Renderer


class Button:

    def __init__(
        self,
        size: tuple[float, float],
        coordenate: tuple[float, float],
        text: str,
        window_size: tuple[int, int],
        command,
        font
    ):

        self.width, self.height = size
        self.x, self.y = coordenate
        self.window_w, self.window_h = window_size

        self.text = text
        self.status = True

        self.command = command 

        self.scale_x = 1 / self.window_w
        self.scale_y = 1 / self.window_h

        self.obj_border = None
        self.obj_body = None


        self.Font = None

        self.text_meshes = {}
        self.font_height = 24
        self.font_size = font

        self.viewport_offset_x = 0
        self.command = command

        print("CRIANDO BOTÃO:", self.text)
        print("COMMAND RECEBIDO:", self.command)

    def set_viewport_offset(self, offset_x):

        self.viewport_offset_x = offset_x
        print("OFFSET:", self.text, offset_x)

    def set_status(self, on: bool):

        if on != self.status:
            self.status = on

    def set_widget(self):

        # Agora o OpenGL já existe
        self.Font = FontRenderer(self.font_size)

        self.font_height = self.Font.face.size.height >> 6
        left = (self.x / self.window_w) * 2.0 - 1.0
        right = ((self.x + self.width) / self.window_w) * 2.0 - 1.0

        # Inverte o eixo Y (origem no canto superior esquerdo)
        top = 1.0 - (self.y / self.window_h) * 2.0
        bottom = 1.0 - ((self.y + self.height) / self.window_h) * 2.0


        vertices = np.array([

            [left,  bottom],
            [right, bottom],
            [right, top],
            [left,  top]

        ], dtype=np.float32)



        indices_border = np.array([

            0,1,
            1,2,
            2,3,
            3,0

        ], dtype=np.uint32)



        indices_body = np.array([

            0,1,2,
            2,3,0

        ], dtype=np.uint32)



        self.BodyMesh = Mesh(
            vertices,
            indices_body,
            2,
            GL_TRIANGLES
        )


        self.mesh = Mesh(
            vertices,
            indices_border,
            2,
            GL_LINES
        )


        self.BodyShader = Shader(
            "VSW_button_body.glsl",
            "VFW_button_body.glsl"
        )


        self.shader = Shader(
            "VSW_button.glsl",
            "VFW_button.glsl"
        )


        self.obj_body = Object3D(
            self.BodyMesh,
            self.BodyShader
        )


        self.obj_border = Object3D(
            self.mesh,
            self.shader
        )


        self.render_body = Renderer()
        self.render_border = Renderer()


        self.FontShader = Shader(
            "font_vertex.glsl",
            "font_fragment.glsl"
        )


        self.FontShader.use()

        self.FontShader.set_vec2(
            "screen",
            self.window_w,
            self.window_h
        )

        # textura fica no GL_TEXTURE0
        self.FontShader.set_int(
            "text",
            0
        )
        self.FontShader.set_vec3(
            "textColor",
            1.0,
            1.0,
            1.0
        )


        # ativa transparência da fonte
        glEnable(GL_BLEND)

        glBlendFunc(
            GL_SRC_ALPHA,
            GL_ONE_MINUS_SRC_ALPHA
        )

    def get_text_width(self):

        width = 0
        spacing = 20

        for i, char in enumerate(self.text):

            if char in self.Font.characters:
                glyph = self.Font.characters[char]

                width += glyph.advance >> 6

                if i < len(self.text)-1:
                    width += spacing

        return width + 15
    
    def render_text(self, text, x, y):

        self.FontShader.use()
        self.FontShader.set_int("text", 0)

        cursor_x = x

        for char in text:

            if char not in self.Font.characters:
                continue

            glyph = self.Font.characters[char]

            if char not in self.text_meshes:

                self.text_meshes[char] = TextMesh(
                    glyph.width,
                    glyph.height,
                    self.window_w,
                    self.window_h   
                )

            xpos = cursor_x + glyph.bearing_x
            ypos = y + glyph.height - glyph.bearing_y

            ndc_x = (xpos / self.window_w) * 2.0 - 1.0
            screen_y = self.window_h - ypos
            ndc_y = (screen_y / self.window_h) * 2.0 - 1.0

            self.FontShader.set_vec2(
                "offset",
                ndc_x,
                ndc_y
            )
            glActiveTexture(GL_TEXTURE0)
            glBindTexture(GL_TEXTURE_2D, glyph.texture)
            
            

            self.text_meshes[char].draw()
            
            letter_spacing = 20  # pixels extras entre letras

            cursor_x += (glyph.advance >> 6) + letter_spacing


    def render(self):

        if self.obj_body:
            self.render_body.draw(
                self.obj_body
            )

        if self.obj_border:
            self.render_border.draw(
                self.obj_border
            )

        if self.text:

            text_width = self.get_text_width()

            x = self.x + (self.width - text_width) / 2
            

            # centralização vertical
            font_height = self.Font.face.size.height >> 6
            ascender = self.Font.face.size.ascender >> 6

            y = self.y + (self.height - font_height) / 2 + ascender
            self.render_text(
                self.text,
                x,
                y
            )
                        
                
    import glfw
import numpy as np
from OpenGL.GL import *

from dashboard.libOpenGL.source.mesh import Mesh
from dashboard.libOpenGL.source.shader import Shader
from dashboard.libOpenGL.font.fontRender import FontRenderer
from dashboard.libOpenGL.source.object import Object3D
from dashboard.libOpenGL.font.meshFont import TextMesh
from dashboard.libOpenGL.source.render import Renderer


class Button:

    def __init__(
        self,
        size: tuple[float, float],
        coordenate: tuple[float, float],
        text: str,
        window_size: tuple[int, int],
        command,
        font
    ):

        self.width, self.height = size
        self.x, self.y = coordenate
        self.window_w, self.window_h = window_size

        self.text = text
        self.status = True

        self.command = command 

        self.scale_x = 1 / self.window_w
        self.scale_y = 1 / self.window_h

        self.obj_border = None
        self.obj_body = None


        self.Font = None

        self.text_meshes = {}
        self.font_height = 24
        self.font_size = font

        self.viewport_offset_x = 0
        self.command = command

        print("CRIANDO BOTÃO:", self.text)
        print("COMMAND RECEBIDO:", self.command)

    def set_viewport_offset(self, offset_x):

        self.viewport_offset_x = offset_x

    def set_status(self, on: bool):

        if on != self.status:
            self.status = on

    def set_widget(self):

        self.Font = FontRenderer(self.font_size)

        left = (self.x / self.window_w) * 2.0 - 1.0
        right = ((self.x + self.width) / self.window_w) * 2.0 - 1.0

        top = 1.0 - (self.y / self.window_h) * 2.0
        bottom = 1.0 - ((self.y + self.height) / self.window_h) * 2.0


        vertices = np.array([

            [left,  bottom],
            [right, bottom],
            [right, top],
            [left,  top]

        ], dtype=np.float32)



        indices_border = np.array([

            0,1,
            1,2,
            2,3,
            3,0

        ], dtype=np.uint32)



        indices_body = np.array([

            0,1,2,
            2,3,0

        ], dtype=np.uint32)



        self.BodyMesh = Mesh(
            vertices,
            indices_body,
            2,
            GL_TRIANGLES
        )


        self.mesh = Mesh(
            vertices,
            indices_border,
            2,
            GL_LINES
        )


        self.BodyShader = Shader(
            "VSW_button_body.glsl",
            "VFW_button_body.glsl"
        )


        self.shader = Shader(
            "VSW_button.glsl",
            "VFW_button.glsl"
        )


        self.obj_body = Object3D(
            self.BodyMesh,
            self.BodyShader
        )


        self.obj_border = Object3D(
            self.mesh,
            self.shader
        )


        self.render_body = Renderer()
        self.render_border = Renderer()


        self.FontShader = Shader(
            "font_vertex.glsl",
            "font_fragment.glsl"
        )


        self.FontShader.use()

        self.FontShader.set_vec2(
            "screen",
            self.window_w,
            self.window_h
        )

        # textura fica no GL_TEXTURE0
        self.FontShader.set_int(
            "text",
            0
        )
        self.FontShader.set_vec3(
            "textColor",
            1.0,
            1.0,
            1.0
        )


        # ativa transparência da fonte
        glEnable(GL_BLEND)

        glBlendFunc(
            GL_SRC_ALPHA,
            GL_ONE_MINUS_SRC_ALPHA
        )

        print(
    "BOTAO:",
    self.x,
    self.y,
    self.width,
    self.height
)

    def get_text_width(self):

        width = 0
        spacing = 20

        for i, char in enumerate(self.text):

            if char in self.Font.characters:
                glyph = self.Font.characters[char]

                width += glyph.advance >> 6

                if i < len(self.text)-1:
                    width += spacing

        return width + 15
    
    def render_text(self, text, x, y):

        self.FontShader.use()
        self.FontShader.set_int("text", 0)

        cursor_x = x

        for char in text:

            if char not in self.Font.characters:
                continue

            glyph = self.Font.characters[char]

            if char not in self.text_meshes:

                self.text_meshes[char] = TextMesh(
                    glyph.width,
                    glyph.height,
                    self.window_w,
                    self.window_h   
                )

            xpos = cursor_x + glyph.bearing_x
            ypos = y + glyph.height - glyph.bearing_y

            ndc_x = (xpos / self.window_w) * 2.0 - 1.0
            screen_y = self.window_h - ypos
            ndc_y = (screen_y / self.window_h) * 2.0 - 1.0

            self.FontShader.set_vec2(
                "offset",
                ndc_x,
                ndc_y
            )
            glActiveTexture(GL_TEXTURE0)
            glBindTexture(GL_TEXTURE_2D, glyph.texture)
            
            

            self.text_meshes[char].draw()
            
            letter_spacing = 20  # pixels extras entre letras

            cursor_x += (glyph.advance >> 6) + letter_spacing


    def render(self):

        if self.obj_body:
            self.render_body.draw(
                self.obj_body
            )

        if self.obj_border:
            self.render_border.draw(
                self.obj_border
            )

        if self.text:

            text_width = self.get_text_width()

            x = self.x + (self.width - text_width) / 2
            

            # centralização vertical
            font_height = self.Font.face.size.height >> 6
            ascender = self.Font.face.size.ascender >> 6

            y = self.y + (self.height - font_height) / 2 + ascender
            self.render_text(
                self.text,
                x,
                y
            )
                        
    def mouse_callback(self, window, button, action, mods):

        xpos, ypos = glfw.get_cursor_pos(window)

        # transforma para coordenada local da UI
        xpos -= self.viewport_offset_x


        print(
            "MOUSE:",
            xpos,
            ypos,
            "OFFSET:",
            self.viewport_offset_x
        )


        if (
            button == glfw.MOUSE_BUTTON_LEFT
            and action == glfw.PRESS
            and self.x <= xpos <= self.x + self.width
            and self.y <= ypos <= self.y + self.height
        ):

            print("Botão clicado")

            if self.command:
                self.command()

    def cursor_callback(self, window, xpos, ypos):
        pass