import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper, 2 for scissors.\n"))
computer_choice = random.randint(0, 2)
print(f"computer chose {computer_choice}")

if user_choice == 0 and computer_choice == 2:
    print("You wins")
elif computer_choice > user_choice:
    print("You lose")