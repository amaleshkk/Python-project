number = int(input("Enter a number: "))

total = 0
for sum in range(2, number+1, 2):
    # if sum % 2 == 0:
    total += sum


print(f"The sum of even numbers upto {number} is: {total}")