from flask import render_template
from app import app
from app.models.rps_player import Player
from app.models.rps_game import Game

@app.route('/')
def index():
    return render_template('index.html', title='Rock! Paper! Scissors!', )

@app.route('/rock')
def info():
    return render_template('rock.html', title="Rock!", )

@app.route('/paper')
def paper():
    return render_template('paper.html', title='Paper!')

@app.route('/scissors')
def scissors():
    return render_template('scissors.html', title='Scissors!')

# # setting route to give player 1 choice
# @app.route('/<p1_choice>')
# def rps_p1_choice(p1_choice):
#     player1 = Player("Player 1", p1_choice)
#     if {{ p1_choice }} == "rock":
#         return render_template('rock.html', title="Rock!", )
#     elif {{ p1_choice }} == "paper":
#         return render_template('paper.html', title='Paper!')
#     elif {{ p1_choice }} == "scissors":
#         return render_template('scissors.html', title='Scissors!')

# #  setting route to give player 2 choice
@app.route('/<p1_choice>/<p2_choice>')
def rps(p1_choice, p2_choice):
    player1 = Player("Player 1", p1_choice)
    player2 = Player("Player 2", p2_choice)
    game = Game(player1, player2)
    result = game.determine_winner(player1, player2)
    return render_template('result.html', result = result, title='Result!')


