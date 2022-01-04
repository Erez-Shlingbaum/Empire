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

    def update(self, delta_time_ms: float):
        self.world.update(delta_time_ms)

    def on_draw(self):
        self.clear()
        self.world.draw()
