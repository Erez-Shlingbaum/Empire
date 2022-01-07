import logging

import pyglet
import glooey

import world

class MyLabel(glooey.Label):
    custom_color = '#babdb6'
    custom_font_size = 10
    custom_alignment = 'center'

class GameScreen(glooey.Bin):
    def __init__(self):
        super().__init__()

        world_ = world.World()
        self.add(world_)

        x = MyLabel("aelrkgjalekrjg")
        self.add(x)

    def update(self, delta_time_ms: float):
        self.world.update(delta_time_ms)
