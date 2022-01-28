import logging
import math

import pyglet

import camera
import world
from config import GameConfig

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
