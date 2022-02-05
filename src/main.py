import pyglet

import app.consts as consts
from app.game import Game


def main():
    Game(
        caption=consts.GAME_TITLE,
        fullscreen=consts.FULL_SCREEN,
        width=consts.WINDOW_WIDTH,
        height=consts.WINDOW_HEIGHT
    )
    pyglet.app.run()


if __name__ == "__main__":
    main()
