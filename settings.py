class Settings:
    """Game settings"""
    def __init__(self):
        self.screen_width = 1820
        self.screen_height = 980
        self.bg_color = (21, 13, 51)
        """Ship settings"""
        self.ship_speed = 1.5
        """Bullet settings"""
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (255, 255, 0)
        self.bullets_allowed = 3

