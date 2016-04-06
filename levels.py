from constants import *
from pytmx.util_pygame import load_pygame
__author__ = 'brown'


class Levels:
    levels = []
    current_level = 0
    collision_map = None
    image_map = None

    def __init__(self):
        for x in range(NUMBER_OF_LEVELS):
            tiled_map = load_pygame('levels/lvl'+str(x)+'.tmx')
            self.levels.append(tiled_map)

    def get_collision_map(self):
        self.collision_map = self.levels[self.current_level].layers[1]

    def get_image_map(self):
        self.image_map = self.levels[self.current_level].layers[0]

    def draw_image_map(self, game_display):
        for x, y, tile in self.image_map.tiles():
            rect = (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            game_display.blit(tile, rect)
