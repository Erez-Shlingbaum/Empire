import random

import pygame
from pygame import Surface

import consts
import service_locator
from hexagon import Hexagon
from tile_map import TileMap, Tile, TileType


class World:
    def __init__(self):
        self.config = service_locator.get_game_config()

        # TODO: refactor this to be loaded from a resource service
        grass_image = pygame.image.load(consts.GRASS_IMAGE_PATH).convert_alpha()
        water_image = pygame.image.load(consts.WATER_IMAGE_PATH).convert_alpha()

        # TODO: refactor this to load from a map generator or from a file
        hexagons = [Hexagon(r, q) for r in range(10) for q in range(10)]
        self.tile_map = TileMap(self.config.window_width, self.config.window_height, [
            Tile(x, TileType.Grass, random.choice([grass_image, water_image])) for x in hexagons
        ])

    def update(self, delta_time_ms: float):
        pass

    def draw(self, surface: Surface):
        self.tile_map.draw(surface)
