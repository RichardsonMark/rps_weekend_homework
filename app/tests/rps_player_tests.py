import unittest
from app.models.rps_player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.rps_player = Player("The Rock", "Rock")


#    @unittest.skip("Delete this line to run the test")
    def test_player_has_name(self):
        self.assertEqual("The Rock", self.rps_player.name)

#    @unittest.skip("Delete this line to run the test")
    def test_player_has_choice(self):
        self.assertEqual("Rock", self.rps_player.player_choice)