from empire.hexagon import Hexagon


def complain(name):
    print("FAIL {0}".format(name))


def equal_hex(name, a, b):
    if not (a.q == b.q and a.s == b.s and a.r == b.r):
        complain(name)


def equal_offsetcoord(name, a, b):
    if not (a.col == b.col and a.row == b.row):
        complain(name)


def equal_doubledcoord(name, a, b):
    if not (a.col == b.col and a.row == b.row):
        complain(name)


def equal_int(name, a, b):
    if not (a == b):
        complain(name)


def equal_hex_array(name, a, b):
    equal_int(name, len(a), len(b))
    for i in range(0, len(a)):
        equal_hex(name, a[i], b[i])


def test_hex_arithmetic():
    equal_hex("hex_add", Hexagon(4, -10, 6), Hexagon(1, -3, 2) + Hexagon(3, -7, 4))
    equal_hex("hex_subtract", Hexagon(-2, 4, -2), Hexagon(1, -3, 2) - Hexagon(3, -7, 4))


# TODO
# def test_hex_direction():
#     equal_hex("hex_direction", Hexagon(0, -1, 1), hex_direction(2))


# def test_hex_neighbor():
#     equal_hex("hex_neighbor", Hexagon(1, -3, 2), hex_neighbor(Hexagon(1, -2, 1), 2))

def test_hex_distance():
    equal_int("hex_distance", 7, Hexagon(3, -7, 4).distance(Hexagon(0, 0, 0)))


def test_hex_round():
    a = Hexagon(0.0, 0.0, 0.0)
    b = Hexagon(1.0, -1.0, 0.0)
    c = Hexagon(0.0, -1.0, 1.0)

    # TODO
    # equal_hex("hex_round 1", Hexagon(5, -10, 5),
    #           hex_round(hex_lerp(Hexagon(0.0, 0.0, 0.0), Hexagon(10.0, -20.0, 10.0), 0.5)))
    # equal_hex("hex_round 2", hex_round(a), hex_round(hex_lerp(a, b, 0.499)))
    # equal_hex("hex_round 3", hex_round(b), hex_round(hex_lerp(a, b, 0.501)))

    equal_hex("hex_round 4", a.round(), Hexagon(a.q * 0.4 + b.q * 0.3 + c.q * 0.3, a.r * 0.4 + b.r * 0.3 + c.r * 0.3,
                                                a.s * 0.4 + b.s * 0.3 + c.s * 0.3).round())

    equal_hex("hex_round 5", c.round(), Hexagon(a.q * 0.3 + b.q * 0.3 + c.q * 0.4, a.r * 0.3 + b.r * 0.3 + c.r * 0.4,
                                                a.s * 0.3 + b.s * 0.3 + c.s * 0.4).round())


def test_hex_linedraw():
    equal_hex_array("hex_linedraw",
                    [Hexagon(0, 0, 0), Hexagon(0, -1, 1), Hexagon(0, -2, 2), Hexagon(1, -3, 2), Hexagon(1, -4, 3),
                     Hexagon(1, -5, 4)],
                    Hexagon(0, 0, 0).line(Hexagon(1, -5, 4)))


# TODO:
# def test_layout():
#     h = Hexagon(3, 4, -7)
#     flat = Layout(layout_flat, Point(10.0, 15.0), Point(35.0, 71.0))
#     equal_hex("layout", h, hex_round(pixel_to_hex(flat, hex_to_pixel(flat, h))))
#     pointy = Layout(layout_pointy, Point(10.0, 15.0), Point(35.0, 71.0))
#     equal_hex("layout", h, hex_round(pixel_to_hex(pointy, hex_to_pixel(pointy, h))))


def test_all():
    test_hex_arithmetic()
    # test_hex_direction()
    # test_hex_neighbor()
    test_hex_distance()
    test_hex_round()
    test_hex_linedraw()
    # test_layout()
