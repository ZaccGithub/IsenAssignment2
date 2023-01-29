def guessing_game(guess):
    '''
    Guess a number between 1 and 100
    '''
    answer = 42
    if guess < answer:
        print("Too low")
    elif guess == 42:
        print("You got it!")
    else:
        print("Too high")
