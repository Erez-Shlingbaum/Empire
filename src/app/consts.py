import pyglet

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Images
WATER_IMAGE_PATH = 'assets/water.png'
GRASS_IMAGE_PATH = 'assets/grass.png'

SPLASH_IMAGE_PATH = "assets/splash.png"

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


SPLASH_DURATION_SEC = 5