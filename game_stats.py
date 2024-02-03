class GameStats:
    """Statistics"""
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """Initializing statistics during the game"""
        self.ship_left = self.settings.ship_limit
