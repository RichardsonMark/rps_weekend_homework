from flask import render_template
from app import app
from app.models.rps_player import Player
from app.models.rps_game import Game

@app.route('/')
def index():
    return render_template('index.html', title='Welcome', )

@app.route('/rock')
def info():
    return render_template('rock.html', title="Rock!", )

@app.route('/paper')
def paper():
    return render_template('paper.html', title='Paper!')

@app.route('/scissors')
def scissors():
    return render_template('scissors.html', title='Scissors!')