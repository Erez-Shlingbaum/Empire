import dataclasses

import pygame


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

    def run(self):
        delta_time = 0.0
        self.clock.tick(self.config.fps)
        while not self.is_game_done:
            self.handle_events()
            self.update(delta_time)
            self.render()
            delta_time = self.clock.tick(self.config.fps) / 1000.0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_game_done = True

    def update(self, delta_time: float):
        pass

    def render(self):
        # TODO: throw this example code away
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)

        # Clear screen
        self.screen.fill(WHITE)

        pygame.draw.rect(self.screen, RED, [55, 200, 100, 70], 0)
        pygame.draw.line(self.screen, GREEN, [0, 0], [100, 100], 5)
        pygame.draw.ellipse(self.screen, BLACK, [20, 20, 250, 100], 2)

        # Update screen with what we've drawn
        pygame.display.flip()
