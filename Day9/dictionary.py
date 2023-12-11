programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Function": "A piece of code that you can easily call over and over again",
    "Loop": "The action of doing something over and over again",
}

print(programming_dictionary["Function"])

programming_dictionary["int"] = "Integer datatype"
print(programming_dictionary)

for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])