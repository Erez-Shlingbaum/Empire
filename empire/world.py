import random

import pyglet

import consts
import service_locator
from hexagon import Hexagon
from tile_map import TileMap, TileType, Tile


class World:
    def __init__(self):
        self.config = service_locator.get_game_config()

        # TODO: refactor this to be loaded from a resource service
        grass_image = pyglet.image.load(consts.GRASS_IMAGE_PATH)
        water_image = pyglet.image.load(consts.WATER_IMAGE_PATH)

        # TODO: refactor this to load from a map generator or from a file
        hexagons = [Hexagon(r, q) for r in range(10) for q in range(10)]
        self.tile_map = TileMap(self.config.window_width, self.config.window_height, [
            Tile(random.choice([grass_image, water_image]), TileType.Grass, x) for x in hexagons
        ])

    def update(self, delta_time_ms: float):
        pass

    def draw(self):
        self.tile_map.draw()
