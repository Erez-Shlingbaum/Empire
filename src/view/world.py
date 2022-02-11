import random

import pyglet

import app.consts as consts
from model.hexagon import Hexagon
from view import tile_map
from view.tile_map import TileMap, TileType, Tile


class World:
    def __init__(self):
        # TODO: refactor this to be loaded from a resource service
        grass_image = pyglet.image.load(consts.GRASS_IMAGE_PATH)
        water_image = pyglet.image.load(consts.WATER_IMAGE_PATH)
        self.outline_image = pyglet.image.load('assets/outline.png')

        # TODO: refactor this to load from a map generator or from a file
        hexagons = [Hexagon(r, q) for r in range(15) for q in range(-5, 10)]
        self.tile_map = TileMap(consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT, [
            Tile(random.choice([grass_image, water_image]), TileType.Grass, x) for x in hexagons
        ])

        self.mouse_hexagon = Hexagon(0, 0)

    def update_mouse_hexagon(self, x, y):
        self.mouse_hexagon = tile_map._hexagon_plotter.from_pixel(x, y - 64)

    def update(self, delta_ms: float):
        pass

    def draw(self):
        self.tile_map.draw()
        Tile(self.outline_image, TileType.Grass, self.mouse_hexagon).draw()
