import random

# Creating variable
guess = ""

# Start of the game
print('Welcome to Rock Paper Scissors! \n If you want to end the game, type "end"')


# Game Function
def Start():
    global guess  # Use the global variable

    guess = input('Type your guess  \n Rock, Paper or Scissors?  \n       Type here: ')
    return guess


Start()

types_of_guesses = ('Rock', 'Paper', 'Scissors')
computer_guess = random.choice(types_of_guesses)

if guess.lower() == "end":
    print('Thanks for playing with me!')
else:
    if guess == computer_guess:
        print("It's a tie!")
        Start()
    elif (guess == "Rock" and computer_guess == "Scissors") or \
            (guess == "Scissors" and computer_guess == "Paper") or \
            (guess == "Paper" and computer_guess == "Rock"):
        print("You win!")
        Start()
    elif guess in types_of_guesses:
        print('You lost')
        Start()
    else:
        print('Invalid guess')
        Start()

