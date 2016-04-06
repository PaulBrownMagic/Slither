# Text to Screen functions
from constants import *


class TextObject:
    # Class to place text objects on the screen.

    x_displace = 0
    y_displace = 0
    size = "small"
   
    def __init__(self, text, colour, x_displace=0, y_displace=0, size="small"):
        # Text Object, defaults to small black centered text.
        self.size = size
        self.colour = colour
        self.x_displace = x_displace
        self.y_displace = y_displace
        self.text_surface = None
        self.font = None
        self.text_rect = None

        self.text_obj(text)

    def text_obj(self, text):
        if self.size == "medium":
            self.font = MEDIUM_FONT
        elif self.size == "large":
            self.font = LARGE_FONT
        else:
            self.font = SMALL_FONT
        self.text_surface = self.font.render(text, True, self.colour)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = DISPLAY_WIDTH/2 + self.x_displace, DISPLAY_HEIGHT/2 + self.y_displace

    def text_blit(self, surface):
        surface.blit(self.text_surface, self.text_rect)


class ScoreText(TextObject):

    def __init__(self, text, colour, x_displace=0, y_displace=0, size="small"):
        super().__init__(text, colour, x_displace, y_displace, size)
        self.surface = pygame.Surface((120, 32))
        self.surface.fill(WHITE)
        self.surface.set_alpha(135)

    def update(self, score, surface):
        surface.blit(self.surface, (5, 10))
        self.text_surface = self.font.render("Score: " + str(score), True, self.colour)
        self.text_blit(surface)
