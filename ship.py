import pygame


class Ship():
    """Ship control"""
    def __init__(self, ai_game):
        """Ship and start position initialization"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        """Ship loading"""
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        """Every new ship creation"""
        self.rect.midbottom = self.screen_rect.midbottom

        """Float coordinates of the ship"""
        self.x = float(self.rect.x)

        """Ship moves"""
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates ship moving counting the flag (moving = False)"""
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """Realtime ship position"""
        self.screen.blit(self.image, self.rect)
