import pyglet

import app.fsm as fsm
import world
import camera


class Gameplay(fsm.State):
    """
    The game state in which the game is played
    """
    def __init__(self, fsm):
        super().__init__(fsm)

        self.world = world.World()
        self.camera = camera.Camera()

        self.keys = pyglet.window.key.KeyStateHandler()

    def push_handlers(self):
        self.fsm.window.push_handlers(self.keys)

    def pop_handlers(self):
        self.fsm.window.pop_handlers(self.keys)

    def update(self, delta_ms: float):
        SCROLL_AMOUNT = 10
        if self.keys[pyglet.window.key.A]:
            self.camera.scroll(SCROLL_AMOUNT, 0)
        if self.keys[pyglet.window.key.W]:
            self.camera.scroll(0, -SCROLL_AMOUNT)
        if self.keys[pyglet.window.key.D]:
            self.camera.scroll(-SCROLL_AMOUNT, 0)
        if self.keys[pyglet.window.key.S]:
            self.camera.scroll(0, SCROLL_AMOUNT)

        self.world.update(delta_ms)

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            self.fsm.pop()

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        # This is a good amount, not too much, not too little
        self.camera.zoom(-0.03 if scroll_y > 0 else 0.03)

    def draw(self):
        with self.camera.camera_transformation():
            self.world.draw()