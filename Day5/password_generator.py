# password generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=']

print("Welcome to PyPassword generator!")
p_letters = int(input("How many letters do you want in password: "))
p_numbers = int(input("How many numbers do you want in password: "))
p_symbols = int(input("How many symbols do you want in password: "))

# easy level
# password = ''

# for n in range(1, p_letters + 1):
#     password += random.choice(letters)

# for n in range(1, p_numbers + 1):
#     password += random.choice(numbers)

# for n in range(1, p_symbols + 1):
#     password += random.choice(symbols)
# print(password)

# hard level
password = []

for n in range(1, p_letters + 1):
    password += random.choice(letters)

for n in range(1, p_numbers + 1):
    password += random.choice(numbers)

for n in range(1, p_symbols + 1):
    password.append(random.choice(symbols))

print(password)
random.shuffle(password)

generated_password = ''
for char in password:
    generated_password += char

print(f"Your passsword is: \n {generated_password}")


