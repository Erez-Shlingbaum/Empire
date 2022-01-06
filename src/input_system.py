import enum

import pyglet.window.key


class InputType(enum.IntEnum):
    LEFT = 0
    RIGHT = 1
    DOWN = 2
    UP = 3


keyboard_mouse_input = {
    pyglet.window.key.A: InputType.LEFT,
    pyglet.window.key.D: InputType.RIGHT,
    pyglet.window.key.S: InputType.DOWN,
    pyglet.window.key.W: InputType.UP,
}
