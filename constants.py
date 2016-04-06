# constants for slither
import pygame

# Colour Constants
WHITE =       (255, 255, 255)
RED =         (255,   0,   0)
GREEN =       (  0, 155,   0)
BLUE =        (  0,   0, 255)
BLACK =       (  0,   0,   0)
GOLD =        (255, 155,   0)
BROWN =       (155, 100,   0)
YELLOW =      (255, 255, 255)
LIGHT_GREEN = (200, 255, 200)

# Image Constants
SNAKE_HEAD = pygame.image.load('images/snake_head.png')
SNAKE_TAIL = pygame.image.load('images/snake_tail.png')
APPLE = pygame.image.load('images/apple.png')
ICON = pygame.image.load('images/icon.png')

# Display window and clock
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)

# Game Constants
BLOCK_SIZE = 20  # Sets grid
MAX_SCORE = 50
NUMBER_OF_LEVELS = 8

# Directions for motion and image rotation
LEFT = 1
DOWN = 2
RIGHT = 3
UP = 4

LEAD_DIRECTIONS = (
                    (          0,           0),
                    (-BLOCK_SIZE,           0),  # Left
                    (          0,  BLOCK_SIZE),  # Down
                    ( BLOCK_SIZE,           0),  # Right
                    (          0, -BLOCK_SIZE)   # Up
                    )

# Fonts
SMALL_FONT = pygame.font.SysFont("comicsansms", 25)
MEDIUM_FONT = pygame.font.SysFont("comicsansms", 50)
LARGE_FONT = pygame.font.SysFont("comicsansms", 80)

# Game States indexes: game_states = [game_intro, game_play, game_paused, game_over]
GAME_INTRO = 0
GAME_PLAY = 1
GAME_OVER = 2
GAME_PAUSED = 3
