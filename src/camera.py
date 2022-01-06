import contextlib

import pyglet.gl


class Camera:
    DEFAULT_MIN_ZOOM = 0.5
    DEFAULT_MAX_ZOOM = 1.5

    def __init__(self, min_zoom=DEFAULT_MIN_ZOOM, max_zoom=DEFAULT_MAX_ZOOM):
        self.zoom_level = 1.0
        self.min_zoom = min_zoom
        self.max_zoom = max_zoom
        self.translation_vector = [0, 0, 0]

    def zoom(self, amount: float):
        if self.min_zoom <= self.zoom_level + amount <= self.max_zoom:
            self.zoom_level += amount

    # TODO: consider adding checks for out of bounds scroll
    # It also make sense for me to check if in world class
    def scroll(self, delta_x: float, delta_y: float):
        self.translation_vector[0] += delta_x
        self.translation_vector[1] += delta_y

    @contextlib.contextmanager
    def camera_transformation(self):
        pyglet.gl.glPushMatrix()
        try:
            pyglet.gl.glOrtho(-self.zoom_level, self.zoom_level, -self.zoom_level, self.zoom_level, -1, 1)
            pyglet.gl.glTranslatef(*self.translation_vector)
            yield
        finally:
            pyglet.gl.glPopMatrix()
