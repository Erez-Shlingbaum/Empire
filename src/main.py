import pyglet

import consts
import app.game as game


def main():
    game.Game(
        caption=consts.GAME_TITLE,
        fullscreen=consts.FULL_SCREEN,
        width=consts.WINDOW_WIDTH,
        height=consts.WINDOW_HEIGHT
    )
    pyglet.app.run()


if __name__ == "__main__":
    main()
