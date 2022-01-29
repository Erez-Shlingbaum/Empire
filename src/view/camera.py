import contextlib

import pyglet.gl
from pyglet.math import Vec3


class Camera:
    """
    2D camera implementation that supports zoom / scroll operations open current Gl matrix transformation
    """
    DEFAULT_MIN_ZOOM = 0.5
    DEFAULT_MAX_ZOOM = 1.5

    def __init__(self, min_zoom=DEFAULT_MIN_ZOOM, max_zoom=DEFAULT_MAX_ZOOM):
        assert 0 < min_zoom <= max_zoom
        self._zoom_level = 1.0
        self.min_zoom = min_zoom
        self.max_zoom = max_zoom
        self.translation_vector = [0, 0, 0]

    @property
    def zoom_level(self):
        return self._zoom_level

    @zoom_level.setter
    def zoom_level(self, value):
        self._zoom_level = max(min(value, self.max_zoom), self.min_zoom)

    @property
    def position(self):
        return self.translation_vector[0], self.translation_vector[1]

    @position.setter
    def position(self, value):
        assert len(value) == 2
        self.translation_vector = (*value, 0)

    # TODO: consider adding checks for out of bounds scroll
    #  It also make sense for me to check if in world class
    def scroll(self, delta_x: float, delta_y: float):
        self.translation_vector[0] += delta_x
        self.translation_vector[1] += delta_y

    def begin_transform(self):
        pyglet.gl.glTranslatef(*self._get_translation_transformation())
        pyglet.gl.glScalef(*self._get_scale_transformation())

    def end_transform(self):
        pyglet.gl.glScalef(*self._get_reverse_scale_transformation())
        pyglet.gl.glTranslatef(*self._get_reverse_translation_transformation())

    def get_transformation_matrix(self):
        return pyglet.math.Mat4.from_translation(self._get_translation_transformation()).scale(
            *self._get_scale_transformation())

    def _get_translation_transformation(self) -> Vec3:
        return Vec3(-self.translation_vector[0] * self._zoom_level, -self.translation_vector[1] * self._zoom_level, 0.0)

    def _get_reverse_translation_transformation(self) -> Vec3:
        return Vec3(self.translation_vector[0] * self._zoom_level, self.translation_vector[1] * self._zoom_level, 0.0)

    def _get_scale_transformation(self) -> Vec3:
        return Vec3(self._zoom_level, self._zoom_level, 1.0)

    def _get_reverse_scale_transformation(self) -> Vec3:
        return Vec3(1.0 / self._zoom_level, 1.0 / self._zoom_level, 1.0)

    @contextlib.contextmanager
    def camera_transformation(self):
        self.begin_transform()
        try:
            yield
        finally:
            self.end_transform()
