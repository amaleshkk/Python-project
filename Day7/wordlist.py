import random

word_list = ["apple", "camel", "nothing", "july"]

chosen_word = random.choice(word_list)

# print(chosen_word)
display_list = []
for word in chosen_word:
    display_list.append("_")


guess = input("\nGuess a letter: ").lower()

print(guess)

print(display_list)
for word in chosen_word:
    if word == guess:
        print('found')
    else:
        print('not found')