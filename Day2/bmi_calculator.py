height = float(input("Enter your height (in meters): "))
weight = int(input("Enter your weight (in kg): "))

bmi = (weight) // (height ** 2)

print(f"Your BMI is {round(bmi, 3)}")