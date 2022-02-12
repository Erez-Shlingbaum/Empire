from pyglet.math import Vec2

from utils.math import Mat2


def test_mat2():
    x = Mat2((1, 2, 3, 4))
    y = Mat2((4, 3, 2, 1))

    assert x @ y == Mat2((8, 5, 20, 13))
    assert x @ x != Mat2((8, 5, 20, 13))

    assert x @ Vec2(2, 5) == Vec2(12, 26)

    # TODO: add more tests for operators
