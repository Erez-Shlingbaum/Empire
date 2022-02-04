"""
Finite state machine
"""
from pyglet.window import Window

from app.fsm_state import FsmState
from app.game import Game


class Fsm:
    """
    Finite state machine
    """

    def __init__(self, window: Game):
        super().__init__()
        self._stack = []

        self.window = window

    def push(self, state: FsmState):
        if not isinstance(state, FsmState):
            raise TypeError(f"Only {FsmState.__name__} type objects can be pushed into fsm")

        self._stack.append(state)
        self.window.push_handlers(state)
        state.push_handlers()

    def pop(self):
        self.top.pop_handlers()
        self.window.pop_handlers()
        return self._stack.pop()

    @property
    def top(self):
        if len(self._stack) == 0:
            raise ValueError("state machine is empty")

        return self._stack[-1]

    def __getattr__(self, name: str):
        return getattr(self.top, name)

    def update(self, delta_ms: float):
        return self.top.update(delta_ms)

    def draw(self):
        return self.top.draw()
