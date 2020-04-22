import random


# Easy game level
def easy():
    print("""You have 6 guesses
You're to guess a number between 1 - 10""")
    secret_number = random.randint(1, 10)
    guess_count = 0
    guess_limit = 6
    while guess_count < guess_limit:
        try:
            guess_limit -= 1
            guess = int(input("Guess: "))
            if guess == secret_number:
                print("You got it right")
                break
                # Break guess loop if user is correct
            else:
                print("wrong")
                print(f' you have {guess_limit}' ' guess(es) left')
                # Limit user input to integers
        except ValueError:
            print("Guess only numbers")
    else:
        print("Game over")


# Medium game level
def medium():
    print("""You have 4 guesses
 You're to guess a number between 1 - 20""")
    secret_number = random.randint(1, 20)
    guess_count = 0
    guess_limit = 4
    while guess_count < guess_limit:
        try:
            guess_limit -= 1
            guess = int(input("Guess: "))
            if guess == secret_number:
                print("You got it right")
                break
                # Break guess loop if user is correct
            else:
                print("wrong")
                print(f' you have {guess_limit}' ' guess(es) left')
                # Limit user input to integers
        except ValueError:
            print("Guess only numbers")
    else:
        print("Game over")


# Hard game level
def hard():
    print("""You have 3 guesses
You're to guess a number between 1 - 50""")
    secret_number = random.randint(1, 50)
    guess_count = 0
    guess_limit = 3
    while guess_count < guess_limit:
        try:
            guess_limit -= 1
            guess = int(input("Guess: "))
            if guess == secret_number:
                print("You got it right")
                break
                # Break guess loop if user is correct
            else:
                print("wrong")
                print(f' you have {guess_limit}' ' guess(es) left')
                # Limit user input to integers
        except ValueError:
            print("Guess only numbers")
    else:
        print("Game over")


# welcome message
def welcome():
    # Game instructions
    print("Welcome to the Guessing game ")
    print("There are 3 levels, easy, medium and hard")
    # Collect user difficulty
    guess_level = input("Choose Difficulty, Enter Easy, Medium or Hard: ").upper()
    if guess_level == "HARD":
        hard()
    elif guess_level == "EASY":
        easy()
    elif guess_level == "MEDIUM":
        medium()


# initiate game
welcome()
