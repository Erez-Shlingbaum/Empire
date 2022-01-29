import pyglet

import consts
import app.game as game


def main():
    game.Game(caption=consts.GAME_TITLE, fullscreen=False)
    pyglet.app.run()


if __name__ == "__main__":
    main()
