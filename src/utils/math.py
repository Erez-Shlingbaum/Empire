import dataclasses
from operator import mul as _mul

from pyglet.math import Vec2


@dataclasses.dataclass
class Rectangle:
    x: float
    y: float
    width: float
    height: float

    def contains(self, x: float, y: float) -> bool:
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height


class Mat2(tuple):
    """
    `Mat2` is an immutable 2x2 Matrix, including most common
    operators. Matrix multiplication must be performed using
    the "@" operator.

    Note, this class is incomplete and does not support some feature that pyglet.math.Mat3, etc does support.
    """

    def __new__(cls, values=None) -> 'Mat2':
        """Create a 2x2 Matrix

        A Mat2 can be created with a list or tuple of 4 values.
        If no values are provided, an "identity matrix" will be created
        (1.0 on the main diagonal). Matrix objects are immutable, so
        all operations return a new Mat2 object.

        :Parameters:
            `values` : tuple of float or int
                A tuple or list containing 4 floats or ints.
        """
        assert values is None or len(values) == 4, "A 2x2 Matrix requires 4 values"
        return super().__new__(Mat2, values or (1.0, 0.0,
                                                0.0, 1.0,))

    def __add__(self, other) -> 'Mat2':
        assert len(other) == 4, "Can only add to other Mat2 types"
        return Mat2(tuple(s + o for s, o in zip(self, other)))

    def __sub__(self, other) -> 'Mat2':
        assert len(other) == 4, "Can only subtract from other Mat2 types"
        return Mat2(tuple(s - o for s, o in zip(self, other)))

    def __pos__(self):
        return self

    def __neg__(self) -> 'Mat2':
        return Mat2(tuple(-v for v in self))

    def __round__(self, ndigits=None) -> 'Mat2':
        return Mat2(tuple(round(v, ndigits) for v in self))

    def __mul__(self, other):
        raise NotImplementedError("Please use the @ operator for Matrix multiplication.")

    def __matmul__(self, other) -> 'Mat2':
        assert len(other) in (2, 4), "Can only multiply with Mat2 or Vec2 types"

        if type(other) is Vec2:
            return Vec2(
                self[0] * other[0] + self[1] * other[1],
                self[2] * other[0] + self[3] * other[1]
            )

        # Rows:
        r0 = self[0:2]
        r1 = self[2:4]
        # Columns:
        c0 = other[0::2]
        c1 = other[1::2]

        # Multiply and sum rows * columns:
        return Mat2((sum(map(_mul, r0, c0)),
                     sum(map(_mul, r0, c1)),
                     sum(map(_mul, r1, c0)),
                     sum(map(_mul, r1, c1))))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self[0:2]}\n    {self[2:4]}"
