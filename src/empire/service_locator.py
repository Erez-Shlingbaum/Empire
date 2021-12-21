"""
Based on https://gameprogrammingpatterns.com/service-locator.html

As more services will be added, this module will be responsible for locating them
Separating the serviced class from knowing how or where a service is implemented
"""

import config
import consts


def get_game_config() -> config.GameConfig:
    return config.GameConfig(consts.GAME_TITLE, consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT, consts.FPS)
