import random

def RockPaperScissors():
    types_of_guesses = ('Rock', 'Paper', 'Scissors')

    while True:
        guess = input('Type your guess  \n Rock, Paper or Scissors?  \n       Type here: ')

        if guess.lower() == "end":
            print('Thanks for playing with me!')
            break
        elif guess not in types_of_guesses:
            print('Invalid guess')
        else:
            computer_guess = random.choice(types_of_guesses)

            if guess == computer_guess:
                print("It's a tie!")
            elif (guess == "Rock" and computer_guess == "Scissors") or \
                    (guess == "Scissors" and computer_guess == "Paper") or \
                    (guess == "Paper" and computer_guess == "Rock"):
                print("You win!")
            else:
                print('You lost')

RockPaperScissors()
