import pyglet

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Images
WATER_IMAGE_PATH = 'assets/water.png'
GRASS_IMAGE_PATH = 'assets/grass.png'

# Game config
GAME_TITLE = 'Empire'

_screen = pyglet.canvas.Display().get_default_screen()
WINDOW_WIDTH = _screen.width  # 1500
WINDOW_HEIGHT = _screen.height  # 800
FPS = 60
FULL_SCREEN = True

# Other
DEFAULT_COLOR_KEY = WHITE
