from turtle import Turtle, Screen

tim = Turtle()
tim.shape('turtle')
tim.color('green')
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# dashed line
for _ in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()

