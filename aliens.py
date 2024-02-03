import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """One alien"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load("images/alien_ship.png")
        self.rect = self.image.get_rect()
        self.settings = ai_game.settings

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        """Moving right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def _check_edges(self):
        """Check reaching edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
