import logging
import sys

import pyglet
import glooey

import consts
import service_locator

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

    # empire_game = game_window.Game(**consts.DEFAULT_WINDOW_CONFIG)
    # pyglet.clock.schedule_interval(empire_game.update, 1 / consts.FPS)

    # Setup pyglet resource directory
    pyglet.resource.path = ["../assets"]
    pyglet.resource.reindex()

    window = pyglet.window.Window(fullscreen=False)
    gui = glooey.Gui(window)

    deck = glooey.Deck("main_menu")
    gui.add(deck)

    from main_menu import MainMenu
    from game_screen import GameScreen
    main_menu = MainMenu(deck)
    gameplay = GameScreen()

    deck.add_state("main_menu", main_menu)
    deck.add_state("gameplay", gameplay)

    pyglet.app.run()

    _logger.info("Ending empire...")


if __name__ == "__main__":
    main()
