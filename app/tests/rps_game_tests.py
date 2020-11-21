import unittest
from app.models.rps_game import Game
from app.models.rps_player import Player


class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Player 1", "rock")
        self.player2 = Player("Player 2", "rock")
        self.game = Game(self.player1, self.player2)


#   @unittest.skip("Delete this line to run the test")
    def test_no_winner(self):
        self.assertEqual("rock", self.player1.player_choice)
        self.assertEqual("rock", self.player2.player_choice)
        self.assertEqual(None, self.game.determine_winner(self.player1, self.player2))
        
    @unittest.skip("Delete this line to run the test")
    def test_player1_winner_rock(self):
        self.player2 = Player("Player 2", "scissors")
        self.assertEqual("rock", self.player1.player_choice)
        self.assertEqual("scissors", self.player2.player_choice)
        self.assertEqual("Player 1", self.game.determine_winner(self.player1, self.player2))

    @unittest.skip("Delete this line to run the test")
    def test_player1_winner_paper(self):
        self.player1 = Player("Player 1", "paper")
        self.player2 = Player("Player 2", "rock")
        self.assertEqual("paper", self.player1.player_choice)
        self.assertEqual("rock", self.player2.player_choice)
        self.assertEqual("Player 1", self.game.determine_winner(self.player1, self.player2))

    @unittest.skip("Delete this line to run the test")
    def test_player1_winner_scissors(self):
        self.player1 = Player("Player 1", "scissors")
        self.player2 = Player("Player 2", "paper")
        self.assertEqual("scissors", self.player1.player_choice)
        self.assertEqual("paper", self.player2.player_choice)
        self.assertEqual("Player 1", self.game.determine_winner(self.player1, self.player2))


    @unittest.skip("Delete this line to run the test")
    def test_player2_winner_rock(self):
        self.player1 = Player("Player 1", "rock")       
        self.player2 = Player("Player 2", "paper")
        self.assertEqual("rock", self.player1.player_choice)
        self.assertEqual("paper", self.player2.player_choice)
        self.assertEqual("Player 2", self.game.determine_winner(self.player1, self.player2))

    @unittest.skip("Delete this line to run the test")
    def test_player2_winner_paper(self):
        self.player1 = Player("Player 1", "paper")
        self.player2 = Player("Player 2", "scissors")
        self.assertEqual("paper", self.player1.player_choice)
        self.assertEqual("scissors", self.player2.player_choice)
        self.assertEqual("Player 2", self.game.determine_winner(self.player1, self.player2))

    @unittest.skip("Delete this line to run the test")
    def test_player2_winner_scissors(self):
        self.player1 = Player("Player 1", "scissors")
        self.player2 = Player("Player 2", "rock")
        self.assertEqual("scissors", self.player1.player_choice)
        self.assertEqual("rock", self.player2.player_choice)
        self.assertEqual("Player 1", self.game.determine_winner(self.player1, self.player2))
        