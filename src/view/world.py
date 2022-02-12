import random
from typing import Union

import pyglet

import app.consts as consts
from model.hexagon import Hexagon
from view import tile_map
from view.tile_map import TileMap, TileType, Tile


def load_hex_image(image_path: str):
    image = pyglet.image.load(image_path)
    texture = image.get_texture()
    texture.width = tile_map.hexagon_plotter.width
    texture.height = tile_map.hexagon_plotter.height
    return image


class World:
    def __init__(self):
        # TODO: refactor this to be loaded from a resource service
        self.grass_image = load_hex_image(consts.GRASS_IMAGE_PATH)
        self.water_image = load_hex_image(consts.WATER_IMAGE_PATH)
        self.outline_image = load_hex_image(consts.OUTLINE_IMAGE_PATH)

        # TODO: refactor this to load from a map generator or from a file
        hexagons = [Hexagon(r, q) for r in range(15) for q in range(-5, 10)]
        self.tile_map = TileMap(consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT, [
            Tile(*random.choice([(self.grass_image, TileType.Grass), (self.water_image, TileType.Water)]), x) for x in hexagons
        ])

        self._mouse_hexagon = Hexagon(0, 0)

    @property
    def mouse_hexagon(self):
        return self._mouse_hexagon

    @mouse_hexagon.setter
    def mouse_hexagon(self, value: Union[Hexagon, tuple[float, float]]):
        if isinstance(value, Hexagon):
            self._mouse_hexagon = value
        else:
            x, y = value
            # We want mouse to be in the middle of the hexagon
            x -= tile_map.hexagon_plotter.size
            y -= tile_map.hexagon_plotter.height / 2
            self._mouse_hexagon = tile_map.hexagon_plotter.world_to_hex(x, y)

    def update(self, delta_ms: float):
        pass

    def draw(self):
        self.tile_map.draw()
        Tile(self.outline_image, TileType.Outline, self._mouse_hexagon).draw()
