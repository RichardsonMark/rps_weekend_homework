class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

# function to determine the winner of the game. rules =  "rock" => "scissors", "scissors" => "paper", "paper" => "rock". draw should be None type
    def determine_winner(self, player1, player2):
        if player1.player_choice == player2.player_choice:
            return None
        # elif p1 choice = rock and p2 choice = scissors or
        # p1 choice = paper and p2 choice = rock or
        # p1 choice = scissors and p2 choice = paper
        # p1 wins
        # elif p1 choice = rock, and p2 choice = paper or
        # p1 choice = paper, and p2 choice = scissors, or
        # p1 choice = scissors and p2 choice = rock, 
        # p2 wins
