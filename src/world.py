import random

import pyglet

import consts

from hexagon import Hexagon
from tile_map import TileMap, TileType, Tile


class World:
    def __init__(self):
        # TODO: refactor this to be loaded from a resource service
        grass_image = pyglet.image.load(consts.GRASS_IMAGE_PATH)
        water_image = pyglet.image.load(consts.WATER_IMAGE_PATH)

        # TODO: refactor this to load from a map generator or from a file
        hexagons = [Hexagon(r, q) for r in range(15) for q in range(-5, 10)]
        self.tile_map = TileMap(consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT, [
            Tile(random.choice([grass_image, water_image]), TileType.Grass, x) for x in hexagons
        ])

    def update(self, delta_ms: float):
        pass

    def draw(self):
        self.tile_map.draw()
