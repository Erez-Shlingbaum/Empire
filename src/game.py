import logging
import math

import pyglet

import camera
import world
from config import GameConfig
from utils.opengl import get_opengl_projection_matrix, normalize_screen_coordinates

_logger = logging.getLogger(__name__)


class Game(pyglet.window.Window):
    def __init__(self, config: GameConfig, *args, **kwargs):
        super().__init__(caption=config.title, width=config.window_width, height=config.window_height,
                         fullscreen=config.fullscreen, *args, **kwargs)
        self.world = world.World()
        self.fps_display = pyglet.window.FPSDisplay(self)
        self.keys = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.keys)
        self.camera = camera.Camera()

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            self.close()

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        # This is a good amount, not too much, not too little
        self.camera.zoom_level += math.copysign(0.03, scroll_y)

    def on_mouse_press(self, x, y, button, modifiers):
        # Note that camera transform operates on GL_MODELVIEW_MATRIX, which is an identity matrix except when we modify it using with camera.transform()
        # Thus, the following method encapsulates both MODELVIEW_MATRIX and CAMERA_MATRIX
        inverse_transform = ~(self.camera.get_transformation_matrix() @ get_opengl_projection_matrix())
        *mouse, _, _ = inverse_transform @ pyglet.math.Vec4(*normalize_screen_coordinates(x, y), 1.0, 1.0)
        print('Mouse position in world =', mouse)

    def update(self, delta_time_ms: float):
        SCROLL_AMOUNT = 10
        if self.keys[pyglet.window.key.A]:
            self.camera.scroll(-SCROLL_AMOUNT, 0)
        if self.keys[pyglet.window.key.W]:
            self.camera.scroll(0, SCROLL_AMOUNT)
        if self.keys[pyglet.window.key.D]:
            self.camera.scroll(SCROLL_AMOUNT, 0)
        if self.keys[pyglet.window.key.S]:
            self.camera.scroll(0, -SCROLL_AMOUNT)

        self.world.update(delta_time_ms)

    def on_draw(self):
        with self.camera.camera_transformation():
            self.clear()
            self.world.draw()
            self.fps_display.draw()
