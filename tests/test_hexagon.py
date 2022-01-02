from hexagon import Hexagon


def test_hex_arithmetic():
    a = Hexagon(4, -10, 6)
    b = Hexagon(1, -3, 2) + Hexagon(3, -7, 4)
    assert a == b

    a1 = Hexagon(-2, 4, -2)
    b1 = Hexagon(1, -3, 2) - Hexagon(3, -7, 4)
    assert a1 == b1


def test_hex_neighbors():
    origin = Hexagon(1, -3)
    neighbors = origin.neighbors()

    assert Hexagon(1, -4) in neighbors
    assert Hexagon(2, -4) in neighbors
    assert Hexagon(2, -3) in neighbors
    assert Hexagon(1, -2) in neighbors
    assert Hexagon(0, -2) in neighbors
    assert Hexagon(0, -3) in neighbors


def test_hex_distance():
    assert 7 == Hexagon(3, -7, 4).distance(Hexagon(0, 0, 0))


def test_hex_round():
    a = Hexagon(0.0, 0.0, 0.0)
    b = Hexagon(1.0, -1.0, 0.0)
    c = Hexagon(0.0, -1.0, 1.0)

    a1 = a.round()
    b1 = Hexagon(a.q * 0.4 + b.q * 0.3 + c.q * 0.3, a.r * 0.4 + b.r * 0.3 + c.r * 0.3,
                 a.s * 0.4 + b.s * 0.3 + c.s * 0.3).round()
    assert a1 == b1

    a2 = c.round()
    b2 = Hexagon(a.q * 0.3 + b.q * 0.3 + c.q * 0.4, a.r * 0.3 + b.r * 0.3 + c.r * 0.4,
                 a.s * 0.3 + b.s * 0.3 + c.s * 0.4).round()
    assert a2 == b2


def test_hex_linedraw():
    line = Hexagon(0, 0, 0).line(Hexagon(1, -5, 4))
    expected_result = [
        Hexagon(0, 0, 0),
        Hexagon(0, -1, 1),
        Hexagon(0, -2, 2),
        Hexagon(1, -3, 2),
        Hexagon(1, -4, 3),
        Hexagon(1, -5, 4)
    ]

    assert line == expected_result
