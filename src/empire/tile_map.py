import enum
from typing import List

from pygame.sprite import Sprite
from pygame.surface import Surface

from hexagon import Hexagon, HexPlot

HEX_WIDTH, HEX_HEIGHT = 40, 40

_hexagon_plotter = HexPlot(HEX_WIDTH, HEX_HEIGHT)


class TileType(enum.IntEnum):
    Grass = 1
    Water = 2


# TODO: have dict from tile type to tile data (image)
# Possibly create the images from a sprite sheet

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
        # TODO: put in const or get as parameter?
        self.map_surface.set_colorkey((0, 0, 0))

        # TODO: seems to work. interesting
        for tile in self.tiles:
            tile.draw(self.map_surface)

    def draw(self, surface: Surface):
        # for tile in self.tiles:
        #     tile.draw(self.map_surface)
        # TODO: decide what to do with map_surface.
        # Should we blit directly to screen surface each time?
        # Or possibly blit only once to self.map_surface and use it each frane
        surface.blit(self.map_surface, (150, 0))


def load_tile_map(path: str):
    pass
