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

# Calculate the angle to rotate each pentagon
angle = 360 / num_pentagons

# Calculate the distance to move the turtle to the starting point of each pentagon
radius = size / (2 * math.sin(math.pi / 5))  # Radius of the circumscribed circle of the pentagon
center_distance = 2 * radius * math.sin(math.pi / num_pentagons)

# Draw the pattern
for i in range(num_pentagons):
    t.penup()
    t.goto(0, 0)
    t.forward(center_distance)
    t.pendown()
    draw_pentagon(size)
    t.penup()
    t.goto(0, 0)
    t.right(angle)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()