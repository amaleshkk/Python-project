print("Thank You for choosing pizza deliveries!")

size = input("Enter the size of the pizza you want? (S, M or L): ")
add_pepperoni = input("Do you want pepperoni? (Y/N): ")
extra_cheese = input("Do you want extra cheese? (Y/N): ")

bill = 0

if size == 'S':
    bill += 15
    print("You have selected small pizza")
    if add_pepperoni == 'Y':
        bill += 2
elif size == 'M':
    bill += 20
    if add_pepperoni == 'Y':
        bill += 3
elif size == 'L':
    bill += 25
    if add_pepperoni == 'Y':
        bill += 3
else:
    print("Thank you for choosing pizza delivery")

if extra_cheese == 'Y':
    bill += 1


print(f"Your total bill is {bill}")

# name = "amalesh"
# print(name.count("s"))

print("""
 ..---..
 /       \
|         |
:         ;
 \  \~/  /
  `, Y ,'
   |_|_|
   |===|
   |===|
    \_/    Peter Punk
""")