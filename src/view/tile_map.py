import enum
import json
from typing import List

import pyglet

from app import consts
from model.hexagon import Hexagon, HexagonPlotter

hexagon_plotter = HexagonPlotter(consts.HEX_SIZE)


class TileType(enum.IntEnum):
    Grass = 1
    Water = 2
    Outline = 3


tile_type_image_map = {
    TileType.Grass: consts.GRASS_IMAGE_PATH,
    TileType.Water: consts.WATER_IMAGE_PATH,
    TileType.Outline: consts.OUTLINE_IMAGE_PATH,
}


class Tile(pyglet.sprite.Sprite):
    def __init__(self, image, tile_type: TileType, hexagon: Hexagon):
        super().__init__(image)
        self.hexagon = hexagon
        self.tile_type = tile_type
        self.position = hexagon_plotter.hex_to_world(hexagon)


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

    @staticmethod
    def load_tile_map(path: str) -> 'TileMap':
        with open(path, 'r') as file:
            serialized_json = json.loads(file.read())

        from view.world import load_hex_image
        return TileMap(
            width=serialized_json['width'],
            height=serialized_json['height'],
            tiles=[Tile(load_hex_image(tile_type_image_map[TileType(tile['tile_type'])]), TileType(tile['tile_type']),
                        Hexagon(*tile['hexagon'])) for tile in serialized_json['tiles']]
        )

    def save_tile_map(self, path: str):
        serialized_json = json.dumps({
            'width': self._width,
            'height': self._height,
            'tiles': [
                {
                    'hexagon': (tile.hexagon.q, tile.hexagon.r, tile.hexagon.s),
                    'tile_type': tile.tile_type
                } for tile in self._tiles
            ]
        })

        with open(path, 'w') as file:
            file.write(serialized_json)
