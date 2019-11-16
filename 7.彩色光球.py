import turtle as t
import random

t.speed('fast')
t.hideturtle()
t.bgcolor('black')

i = 0
temp = ''
colors = ['blue', 'red', 'yellow', 'green', 'cyan', 'purple',
          'white', 'orange', 'brown']

while i < 180:
    rand_color = random.choice(colors)
    while rand_color == temp:
        rand_color = random.choice(colors)
    t.pencolor(rand_color)
    t.penup()
    t.goto(0, 0)
    t.forward(100)
    t.pendown()
    if i % 2 == 0:
        t.forward(300)
    else:
        t.forward(200)
    t.left(2)
    i += 1
    temp = rand_color
