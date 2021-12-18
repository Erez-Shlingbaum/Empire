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

        self.screen.fill(BLACK)

        from hex import Hex, HexPlot
        plotter = HexPlot(40, 40)

        hexes = [Hex(0, 0)]
        hexes += hexes[0].neighbors()

        def _draw_hex(hex):
            from math import pi, sin, cos
            center = plotter.to_pixel(hex)
            center = (center[0] + 250, center[1] + 250)
            verticies = []
            for i in range(6):
                angle = (60 * i) * (pi / 180)
                verticies.append((
                    center[0] + 40 * cos(angle),
                    center[1] + 40 * sin(angle)
                ))

            pygame.draw.polygon(self.screen, WHITE, verticies, width = 2)

        for hex in hexes:
            _draw_hex(hex)

        # Update screen with what we've drawn
        pygame.display.flip()
