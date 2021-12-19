import logging
import sys
from typing import List

import pygame

import game

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


def main(args: List[str]):
    pygame.init()

    try:
        setup_logging(logging.INFO)
        _logger.info("Starting empire...")

        empire_game = game.Game()
        empire_game.run()
        _logger.info("Ending empire...")
    finally:
        pygame.display.quit()
        pygame.quit()


if __name__ == "__main__":
    main(sys.argv[1:])
