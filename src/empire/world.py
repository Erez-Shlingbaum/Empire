import logging
import random

import pygame
from pygame import Surface

import consts
import service_locator
from empire import tile_map
from hexagon import Hexagon
from tile_map import TileMap, Tile, TileType

_logger = logging.getLogger(__name__)


class World:
    def __init__(self):
        self.config = service_locator.get_game_config()
        self.zoom_level = 1

        # TODO: refactor this to be loaded from a resource service
        grass_image = pygame.image.load(consts.GRASS_IMAGE_PATH).convert_alpha()
        water_image = pygame.image.load(consts.WATER_IMAGE_PATH).convert_alpha()

        _logger.info(f'grass_image size = {grass_image.get_size()}')
        _logger.info(f'water_image size = {water_image.get_size()}')

        from tile_map import HEX_WIDTH, HEX_HEIGHT
        # _logger.info(f'expected size = {(HEX_WIDTH * 2, HEX_HEIGHT * 2)}')

        # grass_image = pygame.transform.scale(grass_image, (HEX_WIDTH * 2, HEX_HEIGHT * 2))
        # water_image = pygame.transform.scale(water_image, (HEX_WIDTH * 2, HEX_HEIGHT * 2))
        #
        # _logger.info(f'grass_image size = {grass_image.get_size()}')
        # _logger.info(f'water_image size = {water_image.get_size()}')

        # TODO: refactor this to load from a map generator or from a file
        hexagons = [Hexagon(r, q) for r in range(10) for q in range(10)]
        self.tile_map = TileMap(self.config.window_width, self.config.window_height, [
            Tile(x, TileType.Grass, random.choice([grass_image, water_image])) for x in hexagons
        ])

    def update(self, delta_time_ms: float):
        # Test zoom feature
        # if random.randint(0, 100) == 0:
        if False:
            self.zoom_level = 3

            from tile_map import HEX_WIDTH, HEX_HEIGHT
            tile_map._hexagon_plotter._width = HEX_WIDTH * self.zoom_level
            tile_map._hexagon_plotter._height = HEX_HEIGHT * self.zoom_level

            for tile in self.tile_map.tiles:
                # w, h = tile.image.get_size()
                tile.image = pygame.transform.scale(tile.image,
                                                    (HEX_WIDTH * self.zoom_level, HEX_HEIGHT * self.zoom_level))
                tile.rect = tile.image.get_rect()
                tile.rect.x, tile.rect.y = tile_map._hexagon_plotter.to_pixel(tile.hexagon)

            #             self.image = image
            #         self.rect = self.image.get_rect()
            #         self.rect.x, self.rect.y = _hexagon_plotter.to_pixel(hexagon)

            # w, h = self.grass.get_size()
            # self.grass = pygame.transform.scale(self.grass, (w * self.zoom_level, h * self.zoom_level))
            #
            # w, h = self.water.get_size()
            # self.water = pygame.transform.scale(self.water, (w * self.zoom_level, h * self.zoom_level))

    def draw(self, surface: Surface):
        self.tile_map.draw(surface)
