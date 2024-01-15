import pygame


class Ship():
    """Ship control"""
    def __init__(self, ai_game):
        """Ship and start position initialization"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        """Ship loading"""
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        """Every new ship creation"""
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Realtime ship position"""
        self.screen.blit(self.image, self.rect)
