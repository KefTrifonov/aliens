class Settings:
    """Game settings"""
    def __init__(self):
        self.screen_width = 1820
        self.screen_height = 980
        self.bg_color = (21, 13, 51)
        """Ship settings"""
        self.ship_speed = 1.0
        """Bullet settings"""
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (49, 194, 194)
        self.bullets_allowed = 3
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        """Fleet_direction: 1 - to the right, -1 to the left """
        self.fleet_direction = 1
        self.ship_limit = 3
