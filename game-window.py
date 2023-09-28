from flask import Flask, render_template, request
import random

app = Flask(__name__)


options = ['rock', 'paper', 'scissors']


def play_game(user_choice):
    computer_choice = random.choice(options)
    if user_choice == computer_choice:
        return "It's a Tie!", computer_choice
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return f'Congrats, you win! {user_choice} beats {computer_choice}!!', computer_choice
    else:
        return f'Sorry, you lose! {computer_choice} beats {user_choice}.', computer_choice

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    user_choice = ''
    computer_choice = ''
    
    if request.method == 'POST':
        user_choice = request.form['choice']
        message, computer_choice = play_game(user_choice)
    
    return render_template('index.html', message=message, user_choice=user_choice, computer_choice=computer_choice)

if __name__ == '__main__':
    app.run(debug=True)
