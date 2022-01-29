import app.fsm as fsm
import app.gameplay as gameplay
import consts

import pyglet


class SplashScreen(fsm.State):
    def __init__(self, fsm, duration_sec):
        super().__init__(fsm)

        self._duration_sec = duration_sec
        self._splash_image = pyglet.image.load(consts.SPLASH_IMAGE_PATH)
        self._splash_image.anchor_x = self._splash_image.width // 2
        self._splash_image.anchor_y = self._splash_image.height // 2

        self._splash_title = pyglet.text.Label(
            consts.GAME_TITLE, font_size=36,
            anchor_x="center", anchor_y="center",
            x=self.fsm.window.width // 2,
            y=(self.fsm.window.height // 2) + self._splash_image.height
        )

    def _finish_splash(self):
        gameplay_state = gameplay.Gameplay(self.fsm)

        self.fsm.pop()
        self.fsm.push(gameplay_state)

    def update(self, delta_ms):
        self._duration_sec -= delta_ms

        if self._duration_sec < 0:
            self._finish_splash()

    def draw(self):
        self._splash_image.blit(
            self.fsm.window.width // 2,
            self.fsm.window.height // 2
        )

        self._splash_title.draw()

        pyglet.text.Label(
            str(int(self._duration_sec) + 1), font_size=36,
            anchor_x="center", anchor_y="center",
            x=self.fsm.window.width // 2,
            y=(self.fsm.window.height // 2) - self._splash_image.height
        ).draw()

    def on_key_press(self, symbol, modifiers):
        self._finish_splash()


SplashScreen.register_event_type("on_key_press")