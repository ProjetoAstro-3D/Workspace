from dashboard.libOpenGL.window import CallWindow


def buildOpenGL(queue_TK_OG, queue_OG_TK):

    window = CallWindow(queue_TK_OG, queue_OG_TK)
    window.build()
    window.loop()