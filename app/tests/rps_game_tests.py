import unittest
from app.models.rps_game import Game
from app.models.rps_player import Player


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game("Rock", "Scissors", "Rock defeats Scisors")