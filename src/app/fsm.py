"""
Finite state machine
"""
import abc

import pyglet


class State(pyglet.event.EventDispatcher, metaclass=abc.ABCMeta):
    """
    State in a finite state machine
    """
    def __init__(self, fsm):
        super().__init__()
        self.fsm = fsm

    def push_handlers(self):
        pass

    def pop_handlers(self):
        pass

    @abc.abstractmethod
    def update(self, delta_ms):
        pass

    @abc.abstractmethod
    def draw(self):
        pass


class Fsm:
    """
    """
    def __init__(self, window):
        super().__init__()
        self._stack = []

        self.window = window

    def push(self, state):
        if not isinstance(state, State):
            raise TypeError(f"Only {State.__name__} type objects can be pushed into fsm")

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

    def __getattr__(self, name):
        return self.top.__getattr__(name)

    def update(self, delta_ms):
        return self.top.update(delta_ms)

    def draw(self):
        return self.top.draw()
