import random
from my_module import pi

random_integer = random.randint(1, 230)

print(random_integer)

print(pi)

random_float = random.random()
print(random_float * 5)

coin = ["head", "tail"]

result = random.choice(coin)
print(result)