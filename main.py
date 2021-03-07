# import colorgram
#
# colors = colorgram.extract("image.jpg", 10)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

import turtle
import random

colors = [(234, 166, 59), (45, 112, 157), (113, 150, 203),
          (212, 123, 164), (16, 128, 96), (172, 44, 88),
          (1, 177, 143)]

turtle.colormode(255)

# The following bunch of code controls the turtle behaviour
the_turtle = turtle.Turtle()
the_turtle.speed("fastest")
the_turtle.penup()
the_turtle.hideturtle()

the_screen = turtle.Screen()

# the following bunch sets the initial spot of turtle
the_turtle.setheading(225)
the_turtle.forward(300)
the_turtle.setheading(0)

# the following draws the painting
for dot_count in range(1, 101):
    the_turtle.dot(15, random.choice(colors))
    the_turtle.forward(50)
    if dot_count % 10 == 0:
        the_turtle.setheading(90)
        the_turtle.forward(50)
        the_turtle.setheading(180)
        the_turtle.forward(500)
        the_turtle.setheading(0)

the_screen.exitonclick()
