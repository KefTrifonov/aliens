import sys

from random import randint

from time import sleep

import pygame

from settings import Settings

from ship import Ship

from bullet import Bullet

from aliens import Alien

from stars import Star

from stars_bigger import StarBigger

from game_stats import GameStats


class AlienInvasion:
    """Managing game resources and behavior"""
    def __init__(self):
        """Game initializing and creates game resources"""
        pygame.init()
        self.settings = Settings()
        """Screen settings"""
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        """Ship copy"""
        self.ship = Ship(self)
        """Bullets and aliens groups"""
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.stats = GameStats(self)
        pygame.display.set_caption("Alien Invasion")
        self.stars = pygame.sprite.Group()
        self.stars_ = pygame.sprite.Group()
        self._create_bigger_star_bg()
        self._create_star_bg()

    def run_game(self):
        """Run game"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self.update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        """Put 'stars.draw' upper to draw stars behind of ship and aliens"""
        """Move 'stars.draw' lower to draw stars in front of ship and aliens"""
        self.stars.draw(self.screen)
        self.stars_.draw(self.screen)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            """This string is missed in the book. Without bullet.update_() bullets won't move at all"""
            bullet.update_()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _check_keydown_events(self, event):
        """Keys down events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """Keys up events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        """Aliens and bullets destruction"""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        """Creating an alien fleet"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (40 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        """First row of aliens"""
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """One alien in a row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Reacting when alien reaches edge of the screen"""
        for alien in self.aliens.sprites():
            if alien._check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_star_bg(self):
        """Creating stars grid"""
        star = Star(self)
        star_width, star_height = star.rect.size
#        available_space_x = self.settings.screen_width
        number_stars_x = randint(1, 300)
        available_space_y = self.settings.screen_height + (2 * star_height)
        number_rows = available_space_y // (2 * star_height)

        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """Creating one star in a row"""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.rect.x = star_width + 12 * star_width * star_number
        star.rect.y = star.rect.height + 14 * star.rect.height * row_number

        star.rect.x += randint(-10, 29)
        star.rect.y += randint(-50, 39)

        self.stars.add(star)

    def _create_bigger_star_bg(self):
        """Creating stars grid"""
        star_ = StarBigger(self)
        star__width, star__height = star_.rect.size
#        available_space__x = self.settings.screen_width
        number_stars__x = randint(1, 150)
        available_space__y = self.settings.screen_height - (2 * star__height)
        number__rows = available_space__y // (2 * star__height)

        for row__number in range(number__rows):
            for star__number in range(number_stars__x):
                self._create_star_bigger(star__number, row__number)

    def _create_star_bigger(self, star__number, row__number):
        """Creating one star in a row"""
        star_ = StarBigger(self)
        star__width, star__height = star_.rect.size
        star_.rect.x = star__width + 10 * star__width * star__number
        star_.rect.y = star_.rect.height + 20 * star_.rect.height * row__number

        star_.rect.x += randint(-90, 20)
        star_.rect.y += randint(-1, 700)

        self.stars.add(star_)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Taking one life of the ship"""
        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1
            """Destruction of aliens and bullets after hitting the ship"""
            self.aliens.empty()
            self.bullets.empty()
            """Creating fleet and ship"""
            self._create_fleet()
            self.ship.center_ship()
            """Pause the game after collision"""
            sleep(0.5)
        else:
            self.game_active = False

    def _check_aliens_bottom(self):
        """Checking aliens reaches the bottom"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
