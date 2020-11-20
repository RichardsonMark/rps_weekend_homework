import unittest
from app.models.rps_game import Game
from app.models.rps_player import Player


class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Player 1", "rock")
        self.player2 = Player("Player 2", "scissors")
        self.game = Game(self.player1, self.player2)


#    @unittest.skip("Delete this line to run the test")
    def test_player1_winner(self):
        self.assertEqual("rock", self.player1.player_choice)
        self.assertEqual("scissors", self.player2.player_choice)
        self.assertEqual("Player 1", self.game.determine_winner(self.player1, self.player2))