from flask import render_template, request
from app import app
from app.models.rps_player import Player
from app.models.rps_game import Game
import random

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

# #  setting route to give players choices
@app.route('/<p1_choice>/<p2_choice>')
def rps(p1_choice, p2_choice):
    player1 = Player("Player 1", p1_choice)
    player2 = Player("Player 2", p2_choice)
    game = Game(player1, player2)
    result = game.determine_winner(player1, player2)
    return render_template('result.html', result = result, p1_choice = player1.player_choice, p2_choice = player2.player_choice, title='Result!')


# #  setting route to allow play against the computer
@app.route('/play')
def rps_play():
    options = ["rock", "paper", "scissors"]
    return render_template('/play.html', options=options, title='Play against the computer!')


# #  setting route to return result vs the computer
@app.route('/play/against_computer', methods=['POST'])
def rps_comp():
    player1 = Player(request.form['name'], request.form['options'])
    player2 = Player("Computer", "")
    game = Game(player1, player2)
    options = ["rock", "paper", "scissors"]
    player2.player_choice = options[random.randint(0,2)]

    result_vs_comp = game.determine_winner_vs_comp(player1, player2)

    return render_template("result_vs_comp.html", result_vs_comp = result_vs_comp, name = player1.name, player_choice = player1.player_choice, comp_choice = player2.player_choice, title='Result!')

