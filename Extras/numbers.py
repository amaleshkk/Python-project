numbers = [123, 234, 345, 456, 567]

# i = 0
# for n in numbers:
#     if i == 0:
#         color = "\033[93m"
#         i = 1
#     else:
#         color = "\033[91m"
#         i = 0
#     print(f"{color}{n}")


for i, n in enumerate(numbers):
    if i % 2 == 0:
        color = "\033[93m"
    else:
        color = "\033[91m"
    print(f"{color}{n}")