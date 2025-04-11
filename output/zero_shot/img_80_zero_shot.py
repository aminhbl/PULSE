import turtle
import math

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")

# Function to draw an octagon
def draw_octagon(size):
    for _ in range(8):
        t.forward(size)
        t.left(45)

# Number of octagons
num_octagons = 8
# Size of each octagon
size = 100
# Angle between each octagon
angle = 360 / num_octagons

# Draw the octagons in a circular pattern
for i in range(num_octagons):
    draw_octagon(size)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.left(angle)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()