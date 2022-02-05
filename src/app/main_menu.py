from app import gameplay
from app.fsm import Fsm
from app.fsm_state import FsmState
from gui.clickable_label import ClickableLabel


class MainMenu(FsmState):
    LABEL_PROPERTIES = dict(font_size=36, anchor_x='center', anchor_y='center')

    def __init__(self, fsm: Fsm):
        super().__init__(fsm)
        screen_middle_x = self.fsm.window.width // 2
        screen_middle_y = self.fsm.window.height // 2
        vertical_offset = 100

        self._start_label = ClickableLabel(
            'Start Game', **self.LABEL_PROPERTIES,
            x=screen_middle_x, y=screen_middle_y + vertical_offset
        )

        self._options_label = ClickableLabel(
            'Options', **self.LABEL_PROPERTIES,
            x=screen_middle_x, y=screen_middle_y

        )

        self._exit_label = ClickableLabel(
            'Exit', **self.LABEL_PROPERTIES,
            x=screen_middle_x, y=screen_middle_y - vertical_offset

        )

    def finish_state(self):
        gameplay_state = gameplay.Gameplay(self.fsm)

        self.fsm.pop()
        self.fsm.push(gameplay_state)

    def on_mouse_press(self, x, y, button, modifiers):
        if self._start_label.rect.contains(x, y):
            self.finish_state()
        if self._options_label.rect.contains(x, y):
            print('TODO: options menu')
        if self._exit_label.rect.contains(x, y):
            self.fsm.pop()
            self.fsm.window.dispatch_event('on_close')

    def update(self, delta_ms: float):
        pass

    def draw(self):
        self._start_label.draw()
        self._options_label.draw()
        self._exit_label.draw()


MainMenu.register_event_type('on_mouse_press')
