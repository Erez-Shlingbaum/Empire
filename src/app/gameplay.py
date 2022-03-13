import math

import pyglet

import view.camera as camera
import view.world as world
from app.fsm_state import FsmState
from utils.opengl import screen_to_world_coordinates
from view import tile_map
from view.tile_map import TileType, Tile


class Gameplay(FsmState):
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
        if not self.keys[pyglet.window.key.LCTRL]:
            if self.keys[pyglet.window.key.A]:
                self.camera.scroll(-SCROLL_AMOUNT, 0)
            if self.keys[pyglet.window.key.W]:
                self.camera.scroll(0, SCROLL_AMOUNT)
            if self.keys[pyglet.window.key.D]:
                self.camera.scroll(SCROLL_AMOUNT, 0)
            if self.keys[pyglet.window.key.S]:
                self.camera.scroll(0, -SCROLL_AMOUNT)

        world_x, world_y = screen_to_world_coordinates(self.camera, self.fsm.window._mouse_x, self.fsm.window._mouse_y)
        self.world.mouse_hexagon = (world_x, world_y)
        self.world.update(delta_ms)

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            self.fsm.pop()
            self.fsm.window.dispatch_event('on_close')
        elif (modifiers & pyglet.window.key.MOD_CTRL) and symbol == pyglet.window.key.S:
            self.world.save_world('map.txt')
        elif (modifiers & pyglet.window.key.MOD_CTRL) and symbol == pyglet.window.key.L:
            self.world.load_world('map.txt')
        return True

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        # This is a good amount, not too much, not too little
        self.camera.zoom_level += math.copysign(0.03, scroll_y)
        return True

    def on_mouse_press(self, x, y, button, modifiers):
        # Note that camera transform operates on GL_MODELVIEW_MATRIX, which is an identity matrix except when we modify it using with camera.transform()
        # Thus, the following method encapsulates both MODELVIEW_MATRIX and CAMERA_MATRIX
        mouse = screen_to_world_coordinates(self.camera, x, y)
        self.world.mouse_hexagon = mouse
        print('Mouse position in world =', mouse, 'Hexagon =', self.world.mouse_hexagon)

        for tile in self.world.tile_map.tiles:
            if tile.hexagon == self.world.mouse_hexagon:
                if tile.tile_type == tile_map.TileType.Water:
                    tile.image = self.world.grass_image
                    tile.tile_type = tile_map.TileType.Grass
                    break
                else:
                    tile.image = self.world.water_image
                    tile.tile_type = tile_map.TileType.Water
                    break
        else:
            # TODO: convert tiles to a set
            tile = Tile(self.world.grass_image, TileType.Grass, self.world.mouse_hexagon)
            self.world.tile_map.tiles.append(tile)
            tile.batch = self.world.tile_map

        return True

    def draw(self):
        with self.camera.camera_transformation():
            self.world.draw()


Gameplay.register_event_type("on_key_press")
Gameplay.register_event_type("on_mouse_scroll")
Gameplay.register_event_type("on_mouse_press")
