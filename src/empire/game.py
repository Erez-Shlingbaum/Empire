import dataclasses
import random

import pygame

from empire.hexagon import Hexagon
from empire.tile_map import TileMap, Tile, TileType


@dataclasses.dataclass
class GameConfig:
    title: str
    window_width: int
    window_height: int
    fps: int


class Game:
    def __init__(self, config: GameConfig):
        self.config = config
        self.is_game_done = False
        self.screen = pygame.display.set_mode((config.window_width, config.window_height))
        pygame.display.set_caption(config.title)
        self.clock = pygame.time.Clock()

        # TODO: refactor this
        sheet = pygame.image.load('sheet_really_good.png')

        # Not sure why this is 81 and not some other number
        WIDTH = 156 // 2
        HEIGHT = 66

        # Code to copy specific surface from sprite sheet into a new surface
        # TODO: put in function or sprite sheet class
        rect = pygame.Rect(0, 0, WIDTH, HEIGHT)
        grass_image = pygame.Surface(rect.size).convert()
        grass_image.set_colorkey((0, 0, 0))
        grass_image.blit(sheet, (0, 0), rect)

        rect2 = pygame.Rect(WIDTH, 0, WIDTH, HEIGHT)
        water_image = pygame.Surface(rect2.size).convert()
        water_image.set_colorkey((0, 0, 0))
        water_image.blit(sheet, (0, 0), rect2)

        # TODO: should be in const or something?
        self.screen.set_colorkey((0, 0, 0))

        hexagons = [Hexagon(3 + r, 3) for r in range(6)]

        self.tile_map = TileMap(self.config.window_width, self.config.window_height, [
            Tile(x, TileType.Grass, random.choice([grass_image, water_image])) for x in hexagons
        ])

    def run(self):
        CONVERT_TO_MS = 1000.0
        delta_time_ms = 0.0
        self.clock.tick(self.config.fps)
        while not self.is_game_done:
            self.handle_events()
            self.update(delta_time_ms)
            self.render()
            delta_time_ms = self.clock.tick(self.config.fps) / CONVERT_TO_MS

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_game_done = True

    def update(self, delta_time_ms: float):
        pass

    def render(self):
        WHITE = (255, 255, 255)

        self.screen.fill(WHITE)
        self.tile_map.draw(self.screen)

        pygame.display.flip()
