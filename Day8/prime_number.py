

def prime_number(number):
    is_prime = True 
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime number")
    else:
        print("Not prime")


number = int(input("Enter a number: "))
prime_number(number=number)
