import logging
import sys

import pyglet

import consts
import game
from empire import service_locator

_logger = logging.getLogger(__name__)

LOG_FORMAT = "[%(asctime)s] %(levelname)s:%(name)s: %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def setup_logging(log_level: int):
    """
    Setup basic logging

    :param log_level: minimum log level for emitting messages
    """
    logging.basicConfig(
        level=log_level, stream=sys.stdout, format=LOG_FORMAT, datefmt=LOG_DATE_FORMAT
    )


def main():
    setup_logging(logging.INFO)
    _logger.info("Starting empire...")

    empire_game = game.Game(service_locator.get_game_config())
    pyglet.clock.schedule_interval(empire_game.update, 1 / consts.FPS)
    pyglet.app.run()
    _logger.info("Ending empire...")


if __name__ == "__main__":
    main()
