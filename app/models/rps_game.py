class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

# function to determine the winner of the game. rules =  "rock" => "scissors", "scissors" => "paper", "paper" => "rock". draw should be None type
    def determine_winner(self, player1, player2):
        if self.player1.player_choice == self.player2.player_choice:
            return None
        elif self.player1.player_choice == "rock" and self.player2.player_choice == "scissors" or self.player1.player_choice == "paper" and self.player2.player_choice == "rock" or self.player1.player_choice == "scissors" and self.player2.player_choice == "paper":
            return "Player 1"
        elif self.player1.player_choice == "rock" and self.player2.player_choice == "paper" or self.player1.player_choice == "paper" and self.player2.player_choice == "scissors" or self.player1.player_choice == "scissors" and self.player2.player_choice == "rock":
            return "Player 2"


# play against the computer and determine the winner of the game. As above, rules =  "rock" => "scissors", "scissors" => "paper", "paper" => "rock". draw should be None type
    def determine_winner_vs_comp(self, player1, player2):
        if self.player1.player_choice == self.player2.player_choice:
            return None
        elif self.player1.player_choice == "rock" and self.player2.comp_choice == "scissors" or self.player1.player_choice == "paper" and self.player2.player_choice == "rock" or self.player1.player_choice == "scissors" and self.player2.player_choice == "paper":
            return "Player 1"
        elif self.player1.player_choice == "rock" and self.player2.player_choice == "paper" or self.player1.player_choice == "paper" and self.player2.player_choice == "scissors" or self.player1.player_choice == "scissors" and self.player2.player_choice == "rock":
            return "Computer"