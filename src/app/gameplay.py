import math

import pyglet

import app.fsm as fsm
import world
import camera

from utils.opengl import get_opengl_projection_matrix, normalize_screen_coordinates


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
        self.fsm.window.pop_handlers()

    def update(self, delta_ms: float):
        SCROLL_AMOUNT = 10
        if self.keys[pyglet.window.key.A]:
            self.camera.scroll(-SCROLL_AMOUNT, 0)
        if self.keys[pyglet.window.key.W]:
            self.camera.scroll(0, SCROLL_AMOUNT)
        if self.keys[pyglet.window.key.D]:
            self.camera.scroll(SCROLL_AMOUNT, 0)
        if self.keys[pyglet.window.key.S]:
            self.camera.scroll(0, -SCROLL_AMOUNT)

        self.world.update(delta_ms)

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            self.fsm.pop()

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        # This is a good amount, not too much, not too little
        self.camera.zoom_level += math.copysign(0.03, scroll_y)

    def on_mouse_press(self, x, y, button, modifiers):
        # Note that camera transform operates on GL_MODELVIEW_MATRIX, which is an identity matrix except when we modify it using with camera.transform()
        # Thus, the following method encapsulates both MODELVIEW_MATRIX and CAMERA_MATRIX
        inverse_transform = ~(self.camera.get_transformation_matrix() @ get_opengl_projection_matrix())
        *mouse, _, _ = inverse_transform @ pyglet.math.Vec4(*normalize_screen_coordinates(x, y), 1.0, 1.0)
        print('Mouse position in world =', mouse)

    def draw(self):
        with self.camera.camera_transformation():
            self.world.draw()

Gameplay.register_event_type("on_key_press")
Gameplay.register_event_type("on_mouse_scroll")
Gameplay.register_event_type("on_mouse_press")