from dashboard.libOpenGL.window import CallWindow


def buildOpenGL(queue):
    print("2")

    window = CallWindow()
    window.build()
    window.loop()