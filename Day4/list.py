import random

states = ["kerala", "tamilnadu", "karnataka"]

states.append("MP")

coin = ["head", "tail"]

# states.append(coin)

for state in states:
    print(state)

names = ["Angela", "Ben", "Michael", "Jenny", "Chloe"]

bill_payer = random.choice(names)

print(f"{bill_payer} is going to buy the meal today")

number = len(names)
print(names[number - 1])