# import colorgram
#
#
# rgb_colors = []
# colors = colorgram.extract('image.png', 30)
# for color in colors:
#     # rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as turtle_module
import random



color_list = [(185, 162, 132), (129, 92, 70), (79, 93, 118), (147, 161, 180), (179, 152, 162), (210, 207, 135),
              (28, 35, 49), (119, 79, 92), (54, 24, 33), (46, 25, 19), (147, 170, 154), (86, 107, 91),
              (161, 156, 60), (113, 31, 43), (168, 107, 98), (27, 37, 33), (51, 58, 92), (212, 179, 189),
              (110, 123, 155), (117, 37, 27), (161, 107, 118), (219, 178, 170), (177, 202, 186), (180, 187, 209),
              (106, 144, 116), (67, 75, 35)]

turtle_module.colormode(255)

tim = turtle_module.Turtle()
tim.speed('fastest')
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for i in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()