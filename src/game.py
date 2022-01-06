import logging

import pyglet

import world
from config import GameConfig

_logger = logging.getLogger(__name__)


class Game(pyglet.window.Window):
    def __init__(self, config: GameConfig, *args, **kwargs):
        super().__init__(caption=config.title, width=config.window_width, height=config.window_height,
                         fullscreen=config.fullscreen, *args, **kwargs)
        self.is_game_done = False
        self.world = world.World()
        self.fps_display = pyglet.window.FPSDisplay(self)
        self.keys = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.keys)
        self.zoom = 1

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            self.close()

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        zoom = 1.00
        if scroll_y > 0:
            zoom = 0.97
        elif scroll_y < 0:
            zoom = 1.03

        pyglet.gl.glOrtho(-zoom, zoom, -zoom, zoom, -1, 1)

    def update(self, delta_time_ms: float):
        if self.keys[pyglet.window.key.A]:
            pyglet.gl.glTranslatef(10, 0, 0)
        if self.keys[pyglet.window.key.W]:
            pyglet.gl.glTranslatef(0, -10, 0)
        if self.keys[pyglet.window.key.D]:
            pyglet.gl.glTranslatef(-10, 0, 0)
        if self.keys[pyglet.window.key.S]:
            pyglet.gl.glTranslatef(0, 10, 0)

        self.world.update(delta_time_ms)

    def on_draw(self):
        pyglet.gl.glPushMatrix()
        pyglet.gl.glScalef(self.zoom, self.zoom, 1)

        self.clear()
        self.world.draw()
        self.fps_display.draw()

        pyglet.gl.glPopMatrix()
