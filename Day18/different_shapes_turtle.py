from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape('turtle')
tim.color('green')
tim.speed(2)

colours = ["CornFlowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGrey", "SeaGreen"]

# tim.up()

for num_sides in range(3, 11): 
    tim.color(random.choice(colours))
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)

# tim.circle(100)

screen = Screen()
screen.exitonclick()

# tim.pencolor('blue')
# for _ in range(3):
#     tim.right(120)
#     tim.forward(100)
# tim.pencolor('red')
# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)
# tim.pencolor('yellow')
# for _ in range(5):
#     tim.right(72)
#     tim.forward(100)
# tim.pencolor('orange')
# for _ in range(6):
#     tim.right(60)
#     tim.forward(100)
# tim.pencolor('green')
# for _ in range(7):
#     tim.right(51.43)
#     tim.forward(100)
# tim.pencolor('purple')
# for _ in range(8):
#     tim.right(45)
#     tim.forward(100)
# tim.pencolor('pink')
# for _ in range(9):
#     tim.right(40)
#     tim.forward(100)
# tim.pencolor('brown')
# for _ in range(10):
#     tim.right(36)
#     tim.forward(100)

