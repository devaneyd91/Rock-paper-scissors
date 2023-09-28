import random

game = True

while game is True:
    
    options = ['rock', 'paper', 'scissors']

    computer = random.choice(options)
    user = input('Do you want to play? Type Rock, Paper or Scissors?')
    user = user.lower()    
    
    if user == computer:
        print ('Its a Tie... You wont be so lucky next time!')
    elif user == 'rock' and computer == 'scissors' or user == 'paper' and computer ==  'rock' or user == 'scissors' and computer == 'paper':
        print ('Congrats, you win!', user, 'beats', computer, '!! You have outsmarted this genius code... waah')
    elif computer == 'rock' and user == 'scissors' or computer == 'paper' and user ==  'rock' or computer == 'scissors' and user == 'paper':
        print ('Sorry, you loose!', computer, 'absolutely smashed your pesky', user,'!!! I am UNSTOPPABLE!!!')


    decision = input('Wanna Try Again?? Type yes or no')
    decision = decision.lower()

    if decision == 'yes':
        game = True
    else:
        game = False

if game == False:
    print ('Cool! Thanks for playing')


