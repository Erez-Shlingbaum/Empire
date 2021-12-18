import logging
import sys

import empire
import pygame

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


def main(args):
    pygame.init()

    try:
        setup_logging(logging.INFO)
        _logger.info("Starting empire...")

        empire_game = empire.Game(empire.GameConfig('Empire', 700, 500, 60))
        empire_game.run()
    finally:
        pygame.display.quit()
        pygame.quit()


if __name__ == "__main__":
    main(sys.argv[1:])
