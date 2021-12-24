import enum
from typing import List

from pygame.sprite import Sprite
from pygame.surface import Surface

import consts
from hexagon import Hexagon, HexPlot

# TODO: For now this is just magic,
#   work on realising how to set it properly
#   Also note that the hex images are not a perfect hexagon yet
HEX_WIDTH, HEX_HEIGHT = 63, 74

_hexagon_plotter = HexPlot(HEX_WIDTH, HEX_HEIGHT)


class TileType(enum.IntEnum):
    Grass = 1
    Water = 2


class Tile(Sprite):
    def __init__(self, hexagon: Hexagon, tile_type: TileType, image: Surface):
        super().__init__()
        self.hexagon = hexagon
        self.tile_type = tile_type

        # Override Sprite image, rect
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = _hexagon_plotter.to_pixel(hexagon)

    def draw(self, surface: Surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


class TileMap:
    def __init__(self, width: int, height: int, tiles: List[Tile]):
        self.width = width
        self.height = height
        self.tiles = tiles

        self.map_surface = Surface((self.width, self.height))
        self.map_surface.set_colorkey(consts.DEFAULT_COLOR_KEY)

        # Draw once as the tile map does not change frequently
        self.redraw_map_surface()

    def redraw_map_surface(self):
        self.map_surface.fill(consts.WHITE)
        for tile in self.tiles:
            tile.draw(self.map_surface)

    def draw(self, surface: Surface):
        surface.blit(self.map_surface, (0, 0))


def load_tile_map(path: str) -> TileMap:
    # TODO
    pass
