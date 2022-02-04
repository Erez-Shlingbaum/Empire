from typing import Tuple

import pyglet
from pyglet.math import Mat4

import app.consts as consts


def normalize_screen_coordinates(x, y, screen_width=consts.WINDOW_WIDTH, screen_height=consts.WINDOW_HEIGHT) \
        -> Tuple[float, float]:
    """
    In OpenGL screen coordinates are assumed to be normalized between (-1, 1).
    This method converts x,y from [0, 0], [screen_width, screen_height] to (-1, -1), (1, 1)
    """

    def normalize(fraction: float):
        return 2.0 * fraction - 1.0

    return normalize(x / screen_width), normalize(y / screen_height)


def get_opengl_matrix(matrix_type: int) -> Mat4:
    """
    :param matrix_type: e.g pyglet.gl.GL_PROJECTION_MATRIX, etc.
    """
    matrix = (pyglet.gl.GLfloat * 16)()
    pyglet.gl.glGetFloatv(matrix_type, matrix)
    return Mat4(matrix)
