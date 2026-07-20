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
        size: tuple[int, int],
        coordenate: tuple[int, int],
        text: str
    ):

        self.width, self.height = size
        self.x, self.y = coordenate

        self.text = text
        self.status = True

        self.scale_x = 2 / 400
        self.scale_y = 2 / 300

        self.obj_border = None
        self.obj_body = None


        self.Font = None

        self.text_meshes = {}


    def set_status(self, on: bool):

        if on != self.status:
            self.status = on



    def set_widget(self):

        # Agora o OpenGL já existe
        self.Font = FontRenderer()


        left   = self.x
        right  = self.x + self.width
        bottom = self.y
        top    = self.y + self.height


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

        for char in self.text:

            if char in self.Font.characters:
                width += self.Font.characters[char].advance

        return width



    def render_text(self, text, x, y):

        self.FontShader.use()
        self.FontShader.set_int(
            "text",
            0
        )


        cursor_x = x


        for char in text:


            if char not in self.Font.characters:
                continue


            glyph = self.Font.characters[char]



            if char not in self.text_meshes:


                self.text_meshes[char] = TextMesh(
                    glyph.width * self.scale_x,
                    glyph.height * self.scale_y
                )

                print(glyph.width * self.scale_x,
                    glyph.height * self.scale_y)

            self.FontShader.set_vec2(
                "offset",
                (cursor_x + glyph.bearing_x) * self.scale_x,
                (y - glyph.bearing_y) * self.scale_y
            )



            glActiveTexture(GL_TEXTURE0)


            glBindTexture(
                GL_TEXTURE_2D,
                glyph.texture
            )



            self.text_meshes[char].draw()



            cursor_x += glyph.advance




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


            text_width = self.get_text_width() * self.scale_x


            x = self.x + (
                self.width - text_width
            ) / 2


            y = self.y + self.height / 2



            self.render_text(
                self.text,
                x,
                y
            )