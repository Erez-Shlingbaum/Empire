import enum
from typing import List

import pyglet

from model.hexagon import Hexagon, HexPlot

# TODO: For now this is just magic,
#   work on realising how to set it properly
#   Also note that the hex images are not a perfect hexagon yet
HEX_WIDTH, HEX_HEIGHT = 63, 74

_hexagon_plotter = HexPlot(HEX_WIDTH, HEX_HEIGHT)


class TileType(enum.IntEnum):
    Grass = 1
    Water = 2


class Tile(pyglet.sprite.Sprite):
    def __init__(self, image, tile_type: TileType, hexagon: Hexagon):
        super().__init__(image)
        self.hexagon = hexagon
        self.tile_type = tile_type
        self.position = _hexagon_plotter.to_pixel(hexagon)


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
