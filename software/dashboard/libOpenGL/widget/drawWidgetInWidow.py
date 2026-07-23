from dashboard.libOpenGL.widget.ButtonObj import Button
from dashboard.libOpenGL.widget.BoxText import Text
import glm


class Draw_widget:

    def __init__(
        self,
        window_size,
        window_size_full,
        window,
        viewport_offset,
        obj3D
    ):

        self.window_w, self.window_h = window_size

        self.full_w, self.full_h = window_size_full

        self.window = window

        self.object = obj3D

        self.viewport_offset = viewport_offset


        # valores do objeto

        self.rotate_x = 0
        self.scale = 0.1

        self.position_x = 0
        self.position_z = 0


        self.buttons = []
        self.texts = []


        self.__build()



    # =================================================
    # TRANSFORMAÇÃO DO OBJETO
    # =================================================


    def update_transform(self):

        model = glm.mat4(1.0)


        # escala padrão

        model = glm.scale(
            model,
            glm.vec3(
                self.scale,
                self.scale,
                self.scale
            )
        )


        # rotação original do STL

        model = glm.rotate(
            model,
            glm.radians(180),
            glm.vec3(1,0,0)
        )


        # rotação do usuário

        model = glm.rotate(
            model,
            glm.radians(self.rotate_x),
            glm.vec3(0,1,0)
        )


        # posição

        model = glm.translate(
            model,
            glm.vec3(
                self.position_x,
                -175,
                self.position_z
            )
        )


        self.object.model_r = model



    # =================================================
    # ROTAÇÃO
    # =================================================


    def rotate_x_ms(self):

        if self.rotate_x < 360:

            self.rotate_x += 45

            self.update_transform()

            self.text_valor_rotation_x.set_text(
                str(self.rotate_x)
            )



    def rotate_x_mn(self):

        if self.rotate_x > 0:

            self.rotate_x -= 45

            self.update_transform()

            self.text_valor_rotation_x.set_text(
                str(self.rotate_x)
            )



    # =================================================
    # ESCALA
    # =================================================


    def scale_up(self):

        if self.scale < 0.5:

            self.scale += 0.02

            self.update_transform()

            self.text_valor_scale.set_text(
                str(round(self.scale * 10,1))
            )



    def scale_down(self):

        if self.scale > 0.1:

            self.scale -= 0.02

            self.update_transform()

            self.text_valor_scale.set_text(
                str(round(self.scale * 10,1))
            )



    # =================================================
    # POSIÇÃO X
    # =================================================


    def position_x_up(self):

        if self.position_x < 800:

            self.position_x += 200

            self.update_transform()

            self.text_valor_position_x.set_text(
                str(self.position_x)
            )



    def position_x_down(self):

        if self.position_x > -1000:

            self.position_x -= 200

            self.update_transform()

            self.text_valor_position_x.set_text(
                str(self.position_x)
            )



    # =================================================
    # POSIÇÃO Z
    # =================================================


    def ui_pos(self, x, y):

        return [
            int(self.window_w * x),
            int(self.window_h * y)
        ]


    def ui_size(self, w, h):

        return [
            int(self.window_w * w),
            int(self.window_h * h)
    ]
    def position_z_up(self):

        if self.position_z < 800:

            self.position_z += 200

            self.update_transform()

            self.text_valor_position_z.set_text(
                str(self.position_z)
            )



    def position_z_down(self):

        if self.position_z > -1000:

            self.position_z -= 200

            self.update_transform()

            self.text_valor_position_z.set_text(
                str(self.position_z)
            )



    # =================================================
    # BUILD
    # =================================================


    def __build(self):


        # ==============================
        # TEXTOS
        # ==============================


        self.text_visualizer = Text(
            self.ui_size(0.01, 0.05),
            self.ui_pos(0.01, 0.08),
            "3D Models Visualizer - 200x200mm",
            [self.window_w,self.window_h],
            12
        )


        self.text_Parameter_options = Text(
            self.ui_size(0.25,0.04),
            self.ui_pos(0.02,0.20),
            "Parameter Options:",
            [self.window_w,self.window_h],
            24
        )



        # posições padrões

        label_x = 0.05
        value_x = 0.60

        button_min_x = 0.50
        button_max_x = 0.80



        # Y dos controles

        rotation_y = 0.32
        scale_y = 0.42
        position_x_y = 0.52
        position_z_y = 0.62



        # ==============================
        # ROTATION
        # ==============================


        self.text_rotation_x = Text(
            self.ui_size(0.20,0.04),
            self.ui_pos(label_x,rotation_y),
            "Rotation:",
            [self.window_w,self.window_h],
            16
        )


        self.text_valor_rotation_x = Text(
            self.ui_size(0.05,0.03),
            self.ui_pos(value_x,rotation_y),
            "0",
            [self.window_w,self.window_h],
            20
        )



        # ==============================
        # SCALE
        # ==============================


        self.text_scale = Text(
            self.ui_size(0.20,0.04),
            self.ui_pos(label_x,scale_y),
            "Scale:",
            [self.window_w,self.window_h],
            16
        )


        self.text_valor_scale = Text(
            self.ui_size(0.05,0.03),
            self.ui_pos(value_x,scale_y),
            "1.0",
            [self.window_w,self.window_h],
            20
        )



        # ==============================
        # POSITION X
        # ==============================


        self.text_position_x = Text(
            self.ui_size(0.20,0.04),
            self.ui_pos(label_x,position_x_y),
            "Position X:",
            [self.window_w,self.window_h],
            16
        )


        self.text_valor_position_x = Text(
            self.ui_size(0.05,0.03),
            self.ui_pos(value_x,position_x_y),
            "0",
            [self.window_w,self.window_h],
            20
        )



        # ==============================
        # POSITION Z
        # ==============================


        self.text_position_z = Text(
            self.ui_size(0.20,0.04),
            self.ui_pos(label_x,position_z_y),
            "Position Z:",
            [self.window_w,self.window_h],
            16
        )


        self.text_valor_position_z = Text(
            self.ui_size(0.05,0.03),
            self.ui_pos(value_x,position_z_y),
            "0",
            [self.window_w,self.window_h],
            20
        )



        self.texts.extend([

            self.text_visualizer,
            self.text_Parameter_options,

            self.text_rotation_x,
            self.text_valor_rotation_x,

            self.text_scale,
            self.text_valor_scale,

            self.text_position_x,
            self.text_valor_position_x,

            self.text_position_z,
            self.text_valor_position_z

        ])



        # ==============================
        # BOTÕES
        # ==============================


        button_size = self.ui_size(
            0.045,
            0.045
        )



        # ROTATION

        self.deg_x_mn = Button(
            button_size,
            self.ui_pos(button_min_x,rotation_y),
            "<",
            [self.window_w,self.window_h],
            self.rotate_x_mn,
            24
        )


        self.deg_x_ms = Button(
            button_size,
            self.ui_pos(button_max_x,rotation_y),
            ">",
            [self.window_w,self.window_h],
            self.rotate_x_ms,
            24
        )



        # SCALE

        self.scale_mn = Button(
            button_size,
            self.ui_pos(button_min_x,scale_y),
            "-",
            [self.window_w,self.window_h],
            self.scale_down,
            24
        )


        self.scale_ms = Button(
            button_size,
            self.ui_pos(button_max_x,scale_y),
            "+",
            [self.window_w,self.window_h],
            self.scale_up,
            24
        )



        # POSITION X

        self.position_x_mn = Button(
            button_size,
            self.ui_pos(button_min_x,position_x_y),
            "-",
            [self.window_w,self.window_h],
            self.position_x_down,
            24
        )


        self.position_x_ms = Button(
            button_size,
            self.ui_pos(button_max_x,position_x_y),
            "+",
            [self.window_w,self.window_h],
            self.position_x_up,
            24
        )



        # POSITION Z

        self.position_z_mn = Button(
            button_size,
            self.ui_pos(button_min_x,position_z_y),
            "-",
            [self.window_w,self.window_h],
            self.position_z_down,
            24
        )


        self.position_z_ms = Button(
            button_size,
            self.ui_pos(button_max_x,position_z_y),
            "+",
            [self.window_w,self.window_h],
            self.position_z_up,
            24
        )



        self.buttons.extend([

            self.deg_x_mn,
            self.deg_x_ms,

            self.scale_mn,
            self.scale_ms,

            self.position_x_mn,
            self.position_x_ms,

            self.position_z_mn,
            self.position_z_ms

        ])



        # ==============================
        # INICIALIZAÇÃO
        # ==============================


        for text in self.texts:
            text.set_widget()



        for button in self.buttons:

            button.set_viewport_offset(
                self.viewport_offset
            )

            button.set_widget()



    # =================================================
    # CALLBACKS
    # =================================================


    def mouse_button_callback(
        self,
        window,
        button,
        action,
        mods
    ):

        for widget in self.buttons:

            widget.mouse_callback(
                window,
                button,
                action,
                mods
            )



    def cursor_callback(
        self,
        window,
        xpos,
        ypos
    ):

        for widget in self.buttons:

            if hasattr(widget,"cursor_callback"):

                widget.cursor_callback(
                    window,
                    xpos,
                    ypos
                )



    # =================================================
    # DRAW
    # =================================================


    def draw(self):

        for text in self.texts:
            text.render()


        for button in self.buttons:
            button.render()