import glm

class Camera:

    def __init__(self):

        self.model = glm.mat4(1.0)
        
        self.position = glm.vec3(200, 200, 250)
        self.target = glm.vec3(0, 0, 0)
        self.up = glm.vec3(0, 1, 0)

        self.projection = glm.perspective(
            glm.radians(45.0),
            1.0,
            0.1,
            1000.0
        )

        self.update()

    def update(self):
        self.view = glm.lookAt(
            self.position,
            self.target,
            self.up
        )