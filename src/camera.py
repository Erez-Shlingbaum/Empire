import contextlib

import pyglet.gl


class Camera:
    """2D camera implementation that supports zoom / scroll operations open current Gl matrix transformation"""
    DEFAULT_MIN_ZOOM = 0.5
    DEFAULT_MAX_ZOOM = 1.5

    def __init__(self, min_zoom=DEFAULT_MIN_ZOOM, max_zoom=DEFAULT_MAX_ZOOM):
        assert 0 < min_zoom <= max_zoom, "Minimum zoom must not be greater than maximum zoom"
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
        """Query the current offset."""
        return self.translation_vector[0], self.translation_vector[1]

    @position.setter
    def position(self, value):
        """Set the scroll offset directly."""
        assert len(value) == 2
        self.translation_vector = (*value, 0)

    # TODO: consider adding checks for out of bounds scroll
    #  It also make sense for me to check if in world class
    def scroll(self, delta_x: float, delta_y: float):
        self.translation_vector[0] += delta_x
        self.translation_vector[1] += delta_y

    def begin_transform(self):
        pyglet.gl.glTranslatef(-self.translation_vector[0] * self._zoom_level,
                               -self.translation_vector[1] * self._zoom_level, 0)
        pyglet.gl.glScalef(self._zoom_level, self._zoom_level, 1)

    def end_transform(self):
        pyglet.gl.glScalef(1 / self._zoom_level, 1 / self._zoom_level, 1)
        pyglet.gl.glTranslatef(self.translation_vector[0] * self._zoom_level,
                               self.translation_vector[1] * self._zoom_level, 0)

    @contextlib.contextmanager
    def camera_transformation(self):
        self.begin_transform()
        try:
            yield
        finally:
            self.end_transform()
