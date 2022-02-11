import random

import pyglet

import app.consts as consts
import model
from model.hexagon import Hexagon
from view.tile_map import TileMap, TileType, Tile


def load_hex_image(image_path: str):
    image = pyglet.image.load(image_path)
    texture = image.get_texture()
    texture.width = consts.HEX_WIDTH
    texture.height = consts.HEX_HEIGHT
    return image


class World:
    def __init__(self):
        # TODO: refactor this to be loaded from a resource service
        grass_image = load_hex_image(consts.GRASS_IMAGE_PATH)
        water_image = load_hex_image(consts.WATER_IMAGE_PATH)
        self.outline_image = load_hex_image(consts.OUTLINE_IMAGE_PATH)

        # TODO: refactor this to load from a map generator or from a file
        hexagons = [Hexagon(r, q) for r in range(15) for q in range(-5, 10)]
        self.tile_map = TileMap(consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT, [
            Tile(random.choice([grass_image, water_image]), TileType.Grass, x) for x in hexagons
        ])

        self.mouse_hexagon = Hexagon(0, 0)

    def set_mouse_hexagon(self, x, y):
        self.mouse_hexagon = model.hexagon.from_pixel(x, y)

    def update(self, delta_ms: float):
        pass

    def draw(self):
        self.tile_map.draw()
        Tile(self.outline_image, TileType.Outline, self.mouse_hexagon).draw()
