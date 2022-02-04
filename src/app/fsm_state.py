import abc

import pyglet

from app.fsm import Fsm


class FsmState(pyglet.event.EventDispatcher, metaclass=abc.ABCMeta):
    """
    State in a finite state machine
    """

    def __init__(self, fsm: Fsm):
        super().__init__()
        self.fsm = fsm

    def push_handlers(self):
        pass

    def pop_handlers(self):
        pass

    @abc.abstractmethod
    def update(self, delta_ms: float):
        pass

    @abc.abstractmethod
    def draw(self):
        pass
