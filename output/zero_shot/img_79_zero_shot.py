import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed

# Function to draw a semicircle
def draw_semicircle(radius):
    t.circle(radius, 180)

# Number of semicircles
num_semicircles = 5

# Radius of each semicircle
radius = 100

# Angle between each semicircle
angle_between = 360 / num_semicircles

# Draw the semicircles
for i in range(num_semicircles):
    draw_semicircle(radius)
    t.right(angle_between)

# Hide the turtle
t.hideturtle()

# Finish
turtle.done()