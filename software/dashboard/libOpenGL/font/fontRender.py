import os
import freetype
from OpenGL.GL import *

class Character:
    def __init__(self, texture, width, height, bearing_x, bearing_y, advance):
        self.texture = texture
        self.width = width
        self.height = height
        self.bearing_x = bearing_x
        self.bearing_y = bearing_y
        self.advance = advance


class FontRenderer:

    def __init__(self, font):

        self.base = os.path.dirname(__file__)

        self.path_font = os.path.join(
            self.base,
            "BebasNeue-Regular.ttf"
        )

        self.face = freetype.Face(self.path_font)
        self.face.set_pixel_sizes(0, font)

        self.characters = {}

        self.__load_characters()

    def __load_characters(self):

        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

        # ASCII imprimível
        for ascii_code in range(32, 127):

            char = chr(ascii_code)

            self.face.load_char(char)

            glyph = self.face.glyph

            texture = glGenTextures(1)

            glBindTexture(GL_TEXTURE_2D, texture)

            glTexImage2D(
                GL_TEXTURE_2D,
                0,
                GL_RED,
                glyph.bitmap.width,
                glyph.bitmap.rows,
                0,
                GL_RED,
                GL_UNSIGNED_BYTE,
                glyph.bitmap.buffer
            )

            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)

            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

            self.characters[char] = Character(
                texture=texture,
                width=glyph.bitmap.width,
                height=glyph.bitmap.rows,
                bearing_x=glyph.bitmap_left,
                bearing_y=glyph.bitmap_top,
                advance=glyph.advance.x >> 6
            )

        glBindTexture(GL_TEXTURE_2D, 0)

    # def write(self, text):

    #     x = 0

    #     for char in text:

    #         if char not in self.characters:
    #             continue

    #         glyph = self.characters[char]

    #         glBindTexture(GL_TEXTURE_2D, glyph.texture)

    #         print(
    #             f"Desenhando '{char}' "
    #             f"(Texture={glyph.texture}) "
    #             f"em x={x}"
    #         )

            # Aqui futuramente você fará:
            #
            # 1. Atualizar os vértices do quad
            # 2. glBufferSubData(...)
            # 3. glDrawArrays(GL_TRIANGLES, 0, 6)

            # x += glyph.advance