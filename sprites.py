import random
from constants import *
__author__ = 'brown'


class Snake(pygame.sprite.Sprite):

    def __init__(self):
        self.lead_location = [DISPLAY_WIDTH/2 - DISPLAY_WIDTH/2 % BLOCK_SIZE,
                              DISPLAY_HEIGHT/2 - DISPLAY_HEIGHT/2 % BLOCK_SIZE]
        self.lead_direction = 0
        self.lead_rect = []
        self.snake_blocks = [self.lead_location, self.lead_location]
        self.length = 2
        self.game_over = False
        self.tail = pygame.transform.rotate(SNAKE_TAIL, 0)
        self.head = pygame.transform.rotate(SNAKE_HEAD, 0)

    def reset(self, level):
        self.lead_direction = 0
        self.length = 2
        if level == 4:
            div = 4
        else:
            div = 2
        self.lead_location = [DISPLAY_WIDTH/div - DISPLAY_WIDTH/div % BLOCK_SIZE,
                              DISPLAY_HEIGHT/div - DISPLAY_HEIGHT/div % BLOCK_SIZE]

    def update(self, collision_map):
        super(Snake, self).update()
        self.barriers_check(collision_map)
        self.eating_oneself_check()
        self.grow_the_snake()
        self.find_the_tail()
        self.head_rotate()

    def barriers_check(self, collision_map):
        self.lead_location = [location + direction for location, direction
                              in zip(self.lead_location, LEAD_DIRECTIONS[self.lead_direction])]
        if self.lead_location[0] > DISPLAY_WIDTH - BLOCK_SIZE:
            self.lead_location[0] = 0
        elif self.lead_location[0] < 0:
            self.lead_location[0] = DISPLAY_WIDTH - BLOCK_SIZE
        elif self.lead_location[1] > DISPLAY_HEIGHT - BLOCK_SIZE:
            self.lead_location[1] = 0
        elif self.lead_location[1] < 0:
            self.lead_location[1] = DISPLAY_HEIGHT - BLOCK_SIZE
        x = int(self.lead_location[0] // BLOCK_SIZE)
        y = int(self.lead_location[1] // BLOCK_SIZE)
        if (x, y, 1) in collision_map:
            self.game_over = True
        elif (x, y, 3) in collision_map:
            self.game_over = True

    def eating_oneself_check(self):
        self.lead_rect = self.lead_location + [BLOCK_SIZE, BLOCK_SIZE]
        if self.lead_rect in self.snake_blocks[1:] and self.length > 4:
            self.game_over = True

    def grow_the_snake(self):
        self.snake_blocks.append(self.lead_rect)
        while len(self.snake_blocks) > self.length:
            del self.snake_blocks[0]

    def find_the_tail(self):
        tail_direction = 1
        if len(self.snake_blocks) > 1:
            tail_dir = [t > b for t, b in zip(self.snake_blocks[0], self.snake_blocks[1])]
            if tail_dir == [True, False, False, False]:
                tail_direction = LEFT
            elif tail_dir == [False, True, False, False]:
                tail_direction = UP
            elif tail_dir == [False, False, False, False]:
                tail_dir = [t < b for t, b in zip(self.snake_blocks[0], self.snake_blocks[1])]
                if tail_dir == [True, False, False, False]:
                    tail_direction = RIGHT
                elif tail_dir == [False, True, False, False]:
                    tail_direction = DOWN
                else:
                    tail_direction = 1
            self.tail = pygame.transform.rotate(SNAKE_TAIL, tail_direction * 90)

    def head_rotate(self):
        self.head = pygame.transform.rotate(SNAKE_HEAD, self.lead_direction * 90)

    def draw_the_body(self, game_display):
        for block_rect in self.snake_blocks[1:-1]:
            pygame.draw.rect(game_display, GREEN, block_rect)
            top_left = [block_rect[0], block_rect[1]]
            bottom_right = [block_rect[0] + block_rect[2] - 2, block_rect[1] + block_rect[3] - 2]
            bottom_left = [block_rect[0], block_rect[1] + block_rect[3] - 2]
            top_right = [block_rect[0] + block_rect[2] - 2, block_rect[1]]
            pygame.draw.line(game_display, GOLD, top_left, bottom_right, 2)
            pygame.draw.line(game_display, GOLD, top_right, bottom_left, 2)
            pygame.draw.line(game_display, LIGHT_GREEN, top_left, bottom_left, 1)
            pygame.draw.line(game_display, LIGHT_GREEN, (top_right[0] + 1, top_right[1]),
                                                        (bottom_right[0] + 1, bottom_right[1]), 1)
            pygame.draw.line(game_display, LIGHT_GREEN, top_left, (top_right[0] + 1, top_right[1]), 1)
            pygame.draw.line(game_display, LIGHT_GREEN, (bottom_left[0], bottom_left[1] + 1),
                                                        (bottom_right[0]+1, bottom_right[1] + 1), 1)

    def draw(self, game_display):
        game_display.blit(self.tail, self.snake_blocks[0])
        self.draw_the_body(game_display)
        game_display.blit(self.head, self.snake_blocks[-1])


class Apple(pygame.sprite.Sprite):

    def __init__(self):
        self.apple = APPLE
        self.location = None
        self.rect = None

    def rand_apple_place(self, collision_map):
        x = random.randrange(0, (DISPLAY_WIDTH - BLOCK_SIZE) / BLOCK_SIZE)
        y = random.randrange(0, (DISPLAY_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE)
        while (x, y, 1) in collision_map:
            x = random.randrange(0, (DISPLAY_WIDTH - BLOCK_SIZE) / BLOCK_SIZE)
            y = random.randrange(0, (DISPLAY_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE)
        while (x, y, 3) in collision_map:
            x = random.randrange(0, (DISPLAY_WIDTH - BLOCK_SIZE) / BLOCK_SIZE)
            y = random.randrange(0, (DISPLAY_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE)
        self.location = [x * BLOCK_SIZE, y * BLOCK_SIZE]
        self.rect = self.location + [BLOCK_SIZE, BLOCK_SIZE]

    def draw(self, game_display):
        game_display.blit(self.apple, self.rect)
