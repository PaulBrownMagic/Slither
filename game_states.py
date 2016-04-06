# Game States
import pygame
from text_objects import *
from constants import *
from sprites import *
from levels import *


class GameState:
    clock = pygame.time.Clock()
    game_display = pygame.display.set_mode(DISPLAY_SIZE)
    pygame.display.set_caption('Slither')
    pygame.display.set_icon(ICON)

    def __init__(self):
        self.active = True
        self.events = []
        self.fps = 20
        self.game_exit = False

    def game_quit(self):
        self.game_exit = True

    def event_handling(self):
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                self.game_quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.game_quit()

    def run_logic(self):
        pass

    def display_update(self):
        pass

    def display_flip(self):
        pygame.display.update()
        self.clock.tick(self.fps)


class GameIntro(GameState):

    def __init__(self):
        super().__init__()
        self.fps = 10
        t1 = TextObject("Welcome to Slither", GREEN, y_displace=-130, size="large")
        t2 = TextObject("Eat the apples!", WHITE,  y_displace=-40)
        t3 = TextObject("Don't eat yourself!", WHITE)
        t4 = TextObject("Press C to play, P to pause, or Q to quit", GREEN, y_displace=100, size="small")
        self.text_objects = [t1, t2, t3, t4]

    def event_handling(self):
        super().event_handling()
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    self.active = False

    def display_update(self):
        self.game_display.fill(BLACK)
        for text in self.text_objects:
            text.text_blit(self.game_display)


class GamePause(GameState):

    def __init__(self):
        super().__init__()
        self.surface = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.fps = 10
        self.surface.fill(BLACK)
        self.surface.set_alpha(150)
        self.game_display.blit(self.surface, [0, 0])
        t1 = TextObject("PAUSED", RED, y_displace=-130, size="large")
        t2 = TextObject("Press C to return or Q to quit", RED, y_displace=100, size="medium")
        self.text_objs = [t1, t2]

    def event_handling(self):
        super().event_handling()
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    self.active = False

    def display_update(self):
        for text in self.text_objs:
            text.text_blit(self.game_display)


class GameOver(GameState):

    def __init__(self):
        super().__init__()
        self.surface = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.fps = 10
        self.surface.fill(BLACK)
        self.surface.set_alpha(150)
        self.game_display.blit(self.surface, [0, 0])
        t1 = TextObject("Game Over", RED, y_displace=-130, size="large")
        t2 = TextObject("Press C to play or Q to quit", RED, y_displace=100, size="medium")
        self.text_objs = [t1, t2]

    def event_handling(self):
        super().event_handling()
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    self.active = False

    def display_update(self):
        for text in self.text_objs:
            text.text_blit(self.game_display)


class GamePlay(GameState):

    def __init__(self):
        super().__init__()
        self.fps = 10
        self.snake = Snake()
        self.apple = Apple()
        self.score = 0
        self.score_text = ScoreText("Score: " + str(0), BLACK,
                                    -DISPLAY_WIDTH/2 + 60, -DISPLAY_HEIGHT/2 + 25, "small")
        self.levels = Levels()
        self.levels.get_image_map()
        self.levels.get_collision_map()
        self.apple.rand_apple_place(self.levels.collision_map)

    def event_handling(self):
        super().event_handling()
        moved = False
        for event in self.events:
            if event.type == pygame.KEYDOWN and not moved:
                if event.key == pygame.K_LEFT and self.snake.lead_direction != RIGHT:
                    self.snake.lead_direction = LEFT
                    moved = True
                elif event.key == pygame.K_RIGHT and self.snake.lead_direction != LEFT:
                    self.snake.lead_direction = RIGHT
                    moved = True
                elif event.key == pygame.K_UP and self.snake.lead_direction != DOWN:
                    self.snake.lead_direction = UP
                    moved = True
                elif event.key == pygame.K_DOWN and self.snake.lead_direction != UP:
                    self.snake.lead_direction = DOWN
                    moved = True
                elif event.key == pygame.K_SPACE:
                    self.snake.length = MAX_SCORE + 2

    def run_logic(self):
        self.snake.update(self.levels.collision_map)
        if self.snake.lead_location == self.apple.location:
            self.apple.rand_apple_place(self.levels.collision_map)
            self.snake.length += 1
        self.score = self.snake.length - 2
        if self.snake.game_over:
            self.active = False

    def display_update(self):
        self.levels.draw_image_map(self.game_display)
        self.apple.draw(self.game_display)
        self.snake.draw(self.game_display)
        self.score_text.update(self.score, self.game_display)
