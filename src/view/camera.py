import contextlib

import pyglet.gl
from pyglet.math import Vec3


class Camera:
    """
    2D camera implementation that supports zoom / scroll operations open current Gl matrix transformation
    """
    DEFAULT_MIN_ZOOM = 0.5
    DEFAULT_MAX_ZOOM = 1.5

    def __init__(self, min_zoom: float = DEFAULT_MIN_ZOOM, max_zoom: float = DEFAULT_MAX_ZOOM):
        if not isinstance(min_zoom, float) or not isinstance(max_zoom, float):
            raise TypeError('zoom should be float')
        if not 0 < min_zoom <= max_zoom:
            raise ValueError('min_zoom and max_zoom are invalid')
        self._zoom_level = 1.0
        self.min_zoom = min_zoom
        self.max_zoom = max_zoom
        self.translation_vector = [0, 0, 0]

    @property
    def zoom_level(self):
        return self._zoom_level

    @zoom_level.setter
    def zoom_level(self, value: float):
        if not isinstance(value, float):
            raise TypeError('value should be float')
        self._zoom_level = max(min(value, self.max_zoom), self.min_zoom)

    @property
    def position(self):
        return self.translation_vector[0], self.translation_vector[1]

    @position.setter
    def position(self, value: tuple[float, float]):
        if not isinstance(value, tuple):
            raise TypeError('value should be tuple[float, float]')
        if not len(value) == 2:
            raise ValueError('value should contain 2 floats')
        self.translation_vector = (*value, 0)

    def scroll(self, delta_x: float, delta_y: float):
        self.translation_vector[0] += delta_x
        self.translation_vector[1] += delta_y

    def begin_transform(self):
        pyglet.gl.glTranslatef(*self._translation_transformation)
        pyglet.gl.glScalef(*self._scale_transformation)

    def end_transform(self):
        pyglet.gl.glScalef(*self._reverse_scale_transformation)
        pyglet.gl.glTranslatef(*self._reverse_translation_transformation)

    @property
    def transformation_matrix(self):
        return pyglet.math.Mat4.from_translation(self._translation_transformation).scale(*self._scale_transformation)

    @property
    def _translation_transformation(self) -> Vec3:
        return Vec3(-self.translation_vector[0] * self._zoom_level, -self.translation_vector[1] * self._zoom_level, 0.0)

    @property
    def _reverse_translation_transformation(self) -> Vec3:
        return Vec3(self.translation_vector[0] * self._zoom_level, self.translation_vector[1] * self._zoom_level, 0.0)

    @property
    def _scale_transformation(self) -> Vec3:
        return Vec3(self._zoom_level, self._zoom_level, 1.0)

    @property
    def _reverse_scale_transformation(self) -> Vec3:
        return Vec3(1.0 / self._zoom_level, 1.0 / self._zoom_level, 1.0)

    @contextlib.contextmanager
    def camera_transformation(self):
        self.begin_transform()
        try:
            yield
        finally:
            self.end_transform()
