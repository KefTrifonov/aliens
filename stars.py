import pygame

from pygame.sprite import Sprite


class Star(Sprite):
    """Initializing star on the bg"""
    def __init__(self, star_game):
        """Star position"""
        super().__init__()
        self.screen = star_game.screen

        self.image = pygame.image.load("images/star.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

