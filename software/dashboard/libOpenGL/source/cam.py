import math
import glm

class Camera:

    def __init__(self):

        self.model = glm.mat4(1.0)
        self.angle_y = math.radians(35)

        self.position = glm.vec3(200, 200, 250)
        self.target = glm.vec3(0, 0, 0)
        self.up = glm.vec3(0, 1, 0)

        self.radius = glm.length(self.position - self.target)
        self.angle = math.atan2(
            self.position.z - self.target.z,
            self.position.x - self.target.x
        )

        self.projection = glm.perspective(
            glm.radians(45.0),
            1.0,
            0.1,
            1000.0
        )
        self.height = self.position.y - self.target.y
        self.height_ratio = self.position.y / self.radius
        self.update()

    def update(self):
        self.view = glm.lookAt(
            self.position,
            self.target,
            self.up
        )
    
    def rotate(self, dx, dy):

        sensitivity = 0.01

        self.angle += dx * sensitivity
        self.angle_y += dy * sensitivity

        self.angle_y = max(
            math.radians(10),
            min(math.radians(80), self.angle_y)
        )

        horizontal_radius = self.radius * math.cos(self.angle_y)

        self.position.x = (
            self.target.x +
            horizontal_radius * math.cos(self.angle)
        )

        self.position.z = (
            self.target.z +
            horizontal_radius * math.sin(self.angle)
        )

        self.position.y = (
            self.target.y +
            self.radius * math.sin(self.angle_y)
        )

        self.update()

    def zoom(self, amount):

        self.radius += amount

        self.radius = max(50, min(1000, self.radius))

        self.position.x = (
            self.target.x +
            self.radius * math.cos(self.angle)
        )

        self.position.z = (
            self.target.z +
            self.radius * math.sin(self.angle)
        )

        self.position.y = (
            self.radius * self.height_ratio
        )

        self.update()