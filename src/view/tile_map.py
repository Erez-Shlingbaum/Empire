import enum
from typing import List

import pyglet

import model
from model.hexagon import Hexagon


class TileType(enum.IntEnum):
    Grass = 1
    Water = 2
    Outline = 3


class Tile(pyglet.sprite.Sprite):
    def __init__(self, image, tile_type: TileType, hexagon: Hexagon):
        super().__init__(image)
        self.hexagon = hexagon
        self.tile_type = tile_type
        self.position = model.hexagon.to_pixel(hexagon)


class TileMap(pyglet.graphics.Batch):
    def __init__(self, width: int, height: int, tiles: List[Tile]):
        super().__init__()
        self._width = width
        self._height = height
        self._tiles = tiles

        for tile in tiles:
            tile.batch = self

    @property
    def tiles(self):
        return self._tiles


def load_tile_map(path: str) -> TileMap:
    # TODO
    pass
