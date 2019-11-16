# Layer Cake Challenge - www.101computing.net/layer-cake/
from turtle import *
from shapes import *
import shapes
import time

myPen = Turtle()
myPen.shape("turtle")
myPen.speed(10)
myPen.hideturtle()
window = turtle.Screen()
window.bgcolor("#69D9FF")
y = -140

# Inititalise the dictionary
ingredients = {}
# Add items to the dictionary
ingredients["strawberry"] = "pink"
ingredients["milk chocolate"] = "#BF671F"
ingredients["matcha"] = "#93c572"
ingredients["icing sugar"] = "#FFFFFF"

### Now let's preview the layer cake

# let's draw the plate
draw_rectangle(turtle, "white", -150, y - 10, +300, 10)

# Iterate through each layer of the list
draw_rectangle(myPen, ingredients["milk chocolate"], -120, y, 240, 30)
y += 30
draw_rectangle(myPen, ingredients["strawberry"], -120, y, 240, 35)
y += 35
addIcing(myPen, ingredients["icing sugar"], 120, y)
y += 10
draw_rectangle(myPen, ingredients["milk chocolate"], -100, y, 200, 20)
y += 20
draw_rectangle(myPen, ingredients["strawberry"], -100, y, 200, 40)
y += 40
addIcing(myPen, ingredients["icing sugar"], 100, y)
y += 10
draw_rectangle(myPen, ingredients["milk chocolate"], -70, y, 140, 24)
y += 24
draw_rectangle(myPen, ingredients["strawberry"], -70, y, 140, 36)
y += 36
addIcing(myPen, ingredients["icing sugar"], 70, y)
y += 10
draw_rectangle(myPen, ingredients["matcha"], -4, y, 8, 60)
y += 65
draw_star(myPen, "white", 2, y, 10)

time.sleep(30)
