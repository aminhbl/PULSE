import turtle
import math

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")

# Function to draw a pentagon
def draw_pentagon(size):
    for _ in range(5):
        t.forward(size)
        t.right(72)

# Number of pentagons
num_pentagons = 8

# Size of each pentagon
size = 100

# Angle between each pentagon
angle_between = 360 / num_pentagons

# Calculate the distance to move the turtle to the starting point of each pentagon
distance = size / (2 * math.tan(math.pi / 5))

# Draw the pentagons
for i in range(num_pentagons):
    t.penup()
    t.goto(0, 0)
    t.forward(distance)
    t.pendown()
    draw_pentagon(size)
    t.penup()
    t.goto(0, 0)
    t.right(angle_between)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()