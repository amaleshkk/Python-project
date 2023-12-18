

# Add
def add(num1, num2):
    return num1 + num2

# Subtract
def subtract(num1, num2):
    return num1 - num2

# Multiply
def multiply(num1, num2):
    return num1 * num2

# Divide
def divide(num1, num2):
    return num1 / num2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = 0

for operation in operations:
    print(operation)
operation_symbol = input("Pick and operation from the above: ")

# if operation_symbol == "+":
#     result = add(num1=num1, num2=num2)
# elif operation_symbol == "-":
#     result = subtract(num1=num1, num2=num2)
# elif operation_symbol == "*":
#     result = multiply(num1=num1, num2=num2)
# elif operation_symbol == "/":
#     result = divide(num1=num1, num2=num2)
# else:
#     print("Pick the correct operation from above")

# if result:
#     print(f"{num1} {operation_symbol} {num2} = {result}")

calculation_function = operations[operation_symbol]
answer = calculation_function(num1=num1, num2=num2)