# # import another_module

# # print(another_module.another_variable)

# import turtle
# timmy = turtle.Turtle()

# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.color("green")
# timmy.pencolor("blue")
# timmy.fillcolor("red")
# print(timmy)
# timmy.shape("turtle")
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
# my_screen.delay(12)

# import prettytable

from prettytable import PrettyTable
table = PrettyTable()
# # Method 1
# table.field_names = ["Pokemon Name", "Type"]
# table.add_row(["Pikachu", "Electric"])
# table.add_row(["Squirtle", "Water"])
# table.add_row(["Charmander", "Fire"])

# # Method 2
# table.field_names = ["Pokemon Name", "Type"]
# table.add_rows(
#     [
#         ["Pikachu", "Electric"],
#         ["Squirtle", "Water"],
#         ["Charmander", "Fire"]
#     ]
# )

# Method 3
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

 
table.align = "l"
print(table.align) 

print(table)