# This is a custom module we've made.
# Modules are files full of code that you can import into your programs.
# This one teaches our turtle to draw various shapes.

import turtle
import math


def draw_circle(turtle, color, x, y, radius):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_rectangle(turtle, color, x, y, width, height):
    turtle.hideturtle()
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

    turtle.end_fill()
    turtle.setheading(0)


def draw_star(turtle, color, x, y, size):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.right(144)
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)
        turtle.forward(size)
    turtle.end_fill()
    turtle.setheading(0)


def addIcing(turtle, color, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(-x - 2, y + 10)
    turtle.pendown()
    turtle.begin_fill()

    for z in range(-x - 3, x + 3):
        turtle.goto(z, y - 10 - 10 * math.cos((z / 100) * 2 * math.pi))

    turtle.goto(x + 3, y + 10)
    turtle.goto(-x - 3, y + 10)
    turtle.end_fill()
