from OpenGL.GL import *

from dashboard.libOpenGL.source.shader import Shader
from dashboard.libOpenGL.font.fontRender import FontRenderer
from dashboard.libOpenGL.font.meshFont import TextMesh


class Text:

    def __init__(
        self,
        size: tuple[float, float],
        coordenate: tuple[float, float],
        text: str,
        window_size: tuple[int, int],
        font_size  
    ):

        self.width, self.height = size
        self.x, self.y = coordenate
        self.window_w, self.window_h = window_size
        self.text = text
        self.font_size = font_size

        self.scale_x = 1 / self.window_w
        self.scale_y = 1 / self.window_h

        self.Font = None

        self.text_meshes = {}
        self.font_height = 24

    def set_widget(self):

        # Agora o OpenGL já existe
        self.Font = FontRenderer(self.font_size)

        # Define o tamanho da fonte em pixels
        self.Font.face.set_pixel_sizes(0, self.font_size)

        # Agora as métricas são atualizadas
        self.font_height = self.Font.face.size.height >> 6

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
        spacing = 0

        for i, char in enumerate(self.text):

            if char in self.Font.characters:
                glyph = self.Font.characters[char]

                width += glyph.advance >> 6

                if i < len(self.text)-1:
                    width += spacing

        return width # 15
    
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

            letter_spacing = 15  # pixels extras entre letras

            cursor_x += (glyph.advance >> 6) + letter_spacing


    def render(self):

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
    def set_text(self, new_text: str):
        self.text = str(new_text)

        # opcional:
        # limpa os meshes para reconstruir caso o tamanho das letras mude
        self.text_meshes.clear()