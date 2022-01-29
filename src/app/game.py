import pyglet

import app.fsm as fsm
import app.splash_screen as splash_screen
import consts

class Game(pyglet.window.Window):
    """
    The game main window
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fsm = fsm.Fsm(self)
        splash_state = splash_screen.SplashScreen(self.fsm, consts.SPLASH_DURATION_SEC)
        self.fsm.push(splash_state)

        self.fps_display = pyglet.window.FPSDisplay(self)

        pyglet.clock.schedule_interval(lambda delta_ms: self.fsm.update(delta_ms), 1 / consts.FPS)

    def on_draw(self):
        self.clear()
        self.fsm.draw()
        self.fps_display.draw()
