"""
Hexagons representation module

based on the blogpost https://www.redblobgames.com/grids/hexagons/
"""
# TODO: Evaluate this class for performance, consider using numpy vectors for coordinates, etc

from math import sqrt


class Hex:
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
        return Hex(-self.q, -self.r)

    def __add__(self, other):
        return Hex(self.q + other.q, self.r + other.r)

    def __sub__(self, other):
        return self + (-other)

    def __eq__(self, other):
        return self.q == other.q and self.r == other.r

    def __hash__(self):
        return hash((self.q, self.r))

    def scale(self, scalar):
        """
        Scale coordinates by some factor

        :param scalar: Scaling value
        :type scalar: int / float
        :return: Scaled coordinate
        :rtype: Hex
        """
        return Hex(self.q * scalar, self.r * scalar)

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
        :rtype: list[Hex]
        """
        _DIRECTIONS = [
            Hex(0, -1), Hex(+1, -1), Hex(+1, 0),
            Hex(0, +1), Hex(-1, +1), Hex(-1, 0),
        ]

        return list(map(lambda direction: self + direction, _DIRECTIONS))

    def round(self):
        """
        Round fractional hexagon to the nearest integer coordinate

        :return: The nearest integer hex coordinate
        :rtype: Hex
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

        return Hex(q, r, s)

    def line(self, target):
        """
        Get the hexagons on the line between a source and a target hexagon

        :param target: The target hexagon to reach
        :type target: Hex
        :return: the hexagons between the source and the target
        :rtype: list[Hex]
        """

        # Define a point between 2 1-dimensional values
        def _linear_interpolate(start, end, portion):
            return start + (end - start) * portion

        def _hex_interpolate(start, end, portion):
            return Hex(
                _linear_interpolate(start.q, end.q, portion),
                _linear_interpolate(start.r, end.r, portion),
                _linear_interpolate(start.s, end.s, portion),
            )

        # NOTE: for making rounding rules more deterministic,
        #   use an epsilon value for nuding hexes
        _NUDGE_VALUE = 1e-06
        _NUDGE = Hex(_NUDGE_VALUE, _NUDGE_VALUE)

        distance = self.distance(target)

        return [
            _hex_interpolate(
                self + _NUDGE,
                target + _NUDGE,
                i * (1.0 / distance)
            ).round()
            for i in range(distance + 1)
        ]


# TODO: Should this be seperated from this module?
#   this is representation logic
class HexPlot:
    """
    Conversion from hex logical coordinates to pixel coordinates
    """
    # Flat top pixel conversion
    _TO_PIXEL_MATRIX = (
        (3.0 / 2.0, 0),
        (sqrt(3) / 2.0, sqrt(3))
    )

    # Pixel to hex conversion
    _FROM_PIXEL_MATRIX = (
        (2.0 / 3.0, 0),
        (-1.0 / 3.0, sqrt(3) / 3.0)
    )

    def __init__(self, height: int, width: int):
        """
        :param height: Pixel height of a hexagon
        :param width: Pixel width of a hexagon
        """
        self._height = height
        self._width = width

    @staticmethod
    def _matrix_multiply(matrix, point):
        """
        2x2 matrix multiplication
        """
        return (
            matrix[0][0] * point[0] + matrix[0][1] * point[1],
            matrix[1][0] * point[0] + matrix[1][1] * point[1]
        )

    def to_pixel(self, hexagon):
        """
        Convert Hexagonal coordinate to pixel coordinate
        """
        result = self._matrix_multiply(self._TO_PIXEL_MATRIX, (hexagon.q, hexagon.r))
        return self._width * result[0], self._height * result[1]

    def from_pixel(self, x, y):
        """
        Convert pixel coordinate to hexagonal coordinate
        """
        result = self._matrix_multiply(self._FROM_PIXEL_MATRIX, (x, y))
        return Hex(result[0] / self._width, result[1] / self._height).round()
