import logging

import pygame

import service_locator
from consts import WHITE
from world import World

_logger = logging.getLogger(__name__)


class Game:
    def __init__(self):
        self.config = service_locator.get_game_config()
        self.is_game_done = False
        self.screen = pygame.display.set_mode((self.config.window_width, self.config.window_height))
        pygame.display.set_caption(self.config.title)
        self.clock = pygame.time.Clock()
        self.world = World()

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
        self.world.update(delta_time_ms)

    def render(self):
        self.screen.fill(WHITE)
        self.world.draw(self.screen)
        pygame.display.flip()
