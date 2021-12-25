from empire.hexagon import Hexagon


def equal_hex_array(a, b):
    assert len(a) == len(b)
    for i in range(len(a)):
        assert a[i] == b[i]


def test_hex_arithmetic():
    a = Hexagon(4, -10, 6)
    b = Hexagon(1, -3, 2) + Hexagon(3, -7, 4)
    assert a == b

    a1 = Hexagon(-2, 4, -2)
    b1 = Hexagon(1, -3, 2) - Hexagon(3, -7, 4)
    assert a1 == b1


# TODO
# def test_hex_direction():
#     equal_hex("hex_direction", Hexagon(0, -1, 1), hex_direction(2))


# def test_hex_neighbor():
#     equal_hex("hex_neighbor", Hexagon(1, -3, 2), hex_neighbor(Hexagon(1, -2, 1), 2))

def test_hex_distance():
    assert 7 == Hexagon(3, -7, 4).distance(Hexagon(0, 0, 0))


def test_hex_round():
    a = Hexagon(0.0, 0.0, 0.0)
    b = Hexagon(1.0, -1.0, 0.0)
    c = Hexagon(0.0, -1.0, 1.0)

    # TODO
    # equal_hex("hex_round 1", Hexagon(5, -10, 5),
    #           hex_round(hex_lerp(Hexagon(0.0, 0.0, 0.0), Hexagon(10.0, -20.0, 10.0), 0.5)))
    # equal_hex("hex_round 2", hex_round(a), hex_round(hex_lerp(a, b, 0.499)))
    # equal_hex("hex_round 3", hex_round(b), hex_round(hex_lerp(a, b, 0.501)))

    a1 = a.round()
    b1 = Hexagon(a.q * 0.4 + b.q * 0.3 + c.q * 0.3, a.r * 0.4 + b.r * 0.3 + c.r * 0.3,
                 a.s * 0.4 + b.s * 0.3 + c.s * 0.3).round()
    assert a1 == b1

    a2 = c.round()
    b2 = Hexagon(a.q * 0.3 + b.q * 0.3 + c.q * 0.4, a.r * 0.3 + b.r * 0.3 + c.r * 0.4,
                 a.s * 0.3 + b.s * 0.3 + c.s * 0.4).round()
    assert a2 == b2


def test_hex_linedraw():
    equal_hex_array([
        Hexagon(0, 0, 0),
        Hexagon(0, -1, 1),
        Hexagon(0, -2, 2),
        Hexagon(1, -3, 2),
        Hexagon(1, -4, 3),
        Hexagon(1, -5, 4)
    ], Hexagon(0, 0, 0).line(Hexagon(1, -5, 4)))

# TODO:
# def test_layout():
#     h = Hexagon(3, 4, -7)
#     flat = Layout(layout_flat, Point(10.0, 15.0), Point(35.0, 71.0))
#     equal_hex("layout", h, hex_round(pixel_to_hex(flat, hex_to_pixel(flat, h))))
#     pointy = Layout(layout_pointy, Point(10.0, 15.0), Point(35.0, 71.0))
#     equal_hex("layout", h, hex_round(pixel_to_hex(pointy, hex_to_pixel(pointy, h))))
