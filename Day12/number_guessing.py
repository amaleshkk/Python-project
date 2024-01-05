# import random
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# def guess_func():
#     global choice
#     user_guess = 0
    
#     while(user_guess != answer):
#         print(f"You have {choice} choice left")
#         user_guess = int(input("Guess the number: "))
#         choice -= 1
#         if choice == 0:
#             print("You run out of choices")
#             exit()
#         elif user_guess == answer:
#             print("You have guessed the correct number")
#             exit()
#         elif user_guess > answer:
#             print("Guess is too high")
#         elif user_guess < answer:
#             print("Guess is too low") 

def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


#function to set difficulty
def set_difficulty():
    level = str(input("Choose a difficulty. Type 'easy' or 'hard': "))
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'hard':
        return HARD_LEVEL_TURNS
    
def game():
    print("Welcome to the number Guessing Game!!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining in the guessing game")
        guess = int(input("Guess a number: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of choices")
            exit()
        elif guess != answer:
            print("Guess again")

game()