from math import sqrt

import pyglet

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Images
WATER_IMAGE_PATH = 'assets/water.png'
GRASS_IMAGE_PATH = 'assets/grass.png'
OUTLINE_IMAGE_PATH = 'assets/outline.png'
SPLASH_IMAGE_PATH = "assets/splash.png"

# Hex grid
# size -> distance from middle of hex to a corner
HEX_SIZE = 64.0
HEX_WIDTH = 2.0 * HEX_SIZE
HEX_HEIGHT = sqrt(3.0) * HEX_SIZE

# Game config
GAME_TITLE = 'Empire'

FPS = 120
FULL_SCREEN = False

_screen = pyglet.canvas.Display().get_default_screen()

if FULL_SCREEN:
    WINDOW_WIDTH = _screen.width
    WINDOW_HEIGHT = _screen.height
else:
    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480

# Other
DEFAULT_COLOR_KEY = WHITE

SPLASH_DURATION_SEC = 3
