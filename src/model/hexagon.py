"""
Hexagons representation module

based on the blogpost https://www.redblobgames.com/grids/hexagons/
"""
# TODO: Evaluate this class for performance, consider using numpy vectors for coordinates, etc

from math import sqrt

from pyglet.math import Vec2

from app import consts
from utils.math import Mat2


class Hexagon:
    """
    Hexagon map coordinate
    """

    def __init__(self, q, r, s=None):
        """
        Hexagon with cube / axial coordinates

        :note: coordinates may use fractional / integer values
        :raises ValueError: cube coordinates don't align
        """
        if s is None:
            s = -q - r

        if round(q + r + s) != 0:
            raise ValueError("hex q, r, s sum must be 0")

        self.q = q
        self.r = r
        self.s = s

    def __neg__(self):
        return Hexagon(-self.q, -self.r)

    def __add__(self, other):
        return Hexagon(self.q + other.q, self.r + other.r)

    def __sub__(self, other):
        return self + (-other)

    def __eq__(self, other):
        return self.q == other.q and self.r == other.r and self.s == other.s

    def __hash__(self):
        return hash((self.q, self.r))

    def __repr__(self):
        return "{classname}({q}, {r})".format(classname=self.__class__.__name__, q=self.q, r=self.r)

    def scale(self, scalar):
        """
        Scale coordinates by some factor

        :param scalar: Scaling value
        :type scalar: int / float
        :return: Scaled coordinate
        :rtype: Hexagon
        """
        return Hexagon(self.q * scalar, self.r * scalar)

    def length(self):
        """
        :return: distance from the zero hex
        :rtype: int
        """
        return sum(map(abs, (self.q, self.r, self.s))) // 2

    def distance(self, other):
        return (self - other).length()

    def neighbors(self):
        """
        :return: The hex tiles adjacent to this one
        :rtype: list[Hexagon]
        """
        _DIRECTIONS = [
            Hexagon(0, -1), Hexagon(+1, -1), Hexagon(+1, 0),
            Hexagon(0, +1), Hexagon(-1, +1), Hexagon(-1, 0),
        ]

        return list(map(lambda direction: self + direction, _DIRECTIONS))

    def round(self):
        """
        Round fractional hexagon to the nearest integer coordinate

        :return: The nearest integer hex coordinate
        :rtype: Hexagon
        """
        q = round(self.q)
        r = round(self.r)
        s = round(self.s)

        q_diff = abs(q - self.q)
        r_diff = abs(r - self.r)
        s_diff = abs(s - self.s)

        max_diff = max((q_diff, r_diff, s_diff))
        if q_diff == max_diff:
            q = -r - s
        elif r_diff == max_diff:
            r = -q - s
        else:
            s = -q - r

        return Hexagon(q, r, s)

    def line(self, target):
        """
        Get the hexagons on the line between a source and a target hexagon

        :param target: The target hexagon to reach
        :type target: Hexagon
        :return: the hexagons between the source and the target
        :rtype: list[Hexagon]
        """

        # Define a point between 2 1-dimensional values
        def _linear_interpolate(start, end, portion):
            return start + (end - start) * portion

        def _hex_interpolate(start, end, portion):
            return Hexagon(
                _linear_interpolate(start.q, end.q, portion),
                _linear_interpolate(start.r, end.r, portion),
                _linear_interpolate(start.s, end.s, portion),
            )

        # NOTE: for making rounding rules more deterministic,
        #   use an epsilon value for nudging hexes
        _NUDGE_VALUE = 1e-06
        _NUDGE = Hexagon(_NUDGE_VALUE, _NUDGE_VALUE)

        distance = self.distance(target)

        return [
            _hex_interpolate(
                self + _NUDGE,
                target + _NUDGE,
                i * (1.0 / distance)
            ).round()
            for i in range(distance + 1)
        ]


# Flat top pixel conversion
def to_pixel(hexagon: 'Hexagon', size: float = consts.HEX_SIZE) -> Vec2:
    """
    Convert Hexagonal coordinate to pixel coordinate
    """
    _TO_PIXEL_MATRIX = Mat2(
        (3.0 / 2.0, 0.0,
         sqrt(3.0) / 2.0, sqrt(3.0))
    )
    return (_TO_PIXEL_MATRIX @ Vec2(hexagon.q, hexagon.r)).scale(size)


def from_pixel(x, y, size: float = consts.HEX_SIZE):
    """
    Convert pixel coordinate to hexagonal coordinate
    """
    _FROM_PIXEL_MATRIX = Mat2(
        (2.0 / 3.0, 0.0,
         -1.0 / 3.0, sqrt(3.0) / 3.0)
    )
    x, y = x - 64, y - 64
    q, r = (_FROM_PIXEL_MATRIX @ Vec2(x, y)).scale(1.0 / size)
    return Hexagon(q, r).round()
