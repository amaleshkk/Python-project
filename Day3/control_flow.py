print("Welcome to the rollercoster")
height = int(input("Enter your height in cm: "))
age = int(input("Enter your age: "))

if height >= 120:
    print("You can ride the rollercoaster")
    if age < 12:
        print("Please pay rupees 5")
    elif 12 < age < 18:
        print("Please pay rupees 7")
    else:
        print("Please pay rupees 12")
else:
    print("You cannot ride the rollercoaster")
    