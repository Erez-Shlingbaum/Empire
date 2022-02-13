import pyglet
import pytest

from utils.opengl import get_opengl_matrix
from view.camera import Camera


def test_camera_math():
    camera = Camera(1.0, 5.0)
    start_matrix = camera.transformation_matrix

    camera.scroll(1000, 1000)
    camera.zoom_level = camera.max_zoom

    camera.scroll(-1000, -1000)
    camera.zoom_level = 1.0

    assert start_matrix == camera.transformation_matrix


@pytest.mark.skip(reason='Not really relevant now')
def test_floating_point_error():
    """
    This test fails if for enough camera operations on opengl's matrix, it starts to accumulate floating point error.
    Possible solution: Set opengl's matrix to identity each frame instead of using inverse transformations
    """
    MIN_ZOOM = 1
    MAX_ZOOM = 1000

    start_model_view_matrix = get_opengl_matrix(pyglet.gl.GL_MODELVIEW_MATRIX)

    camera = Camera(MIN_ZOOM, MAX_ZOOM)
    for _ in range(1000):
        camera.scroll(1.001, 1.001)
        camera.zoom_level += 1
        camera.zoom_level %= MAX_ZOOM

        # This modifies using floating point computation opengl's matrix
        with camera.camera_transformation():
            assert start_model_view_matrix != get_opengl_matrix(pyglet.gl.GL_MODELVIEW_MATRIX)
        assert start_model_view_matrix == get_opengl_matrix(pyglet.gl.GL_MODELVIEW_MATRIX)
