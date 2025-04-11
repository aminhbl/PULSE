import turtle
import math

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("white")

# Function to draw a pentagon
def draw_pentagon(side_length):
    for _ in range(5):
        t.forward(side_length)
        t.right(72)

# Function to draw an arc
def draw_arc(radius, extent):
    t.circle(radius, extent)

# Parameters
num_pentagons = 8
pentagon_side = 100
angle_between_pentagons = 360 / num_pentagons
arc_radius = pentagon_side / (2 * math.sin(math.radians(36)))  # Calculate radius for the arc
arc_extent = 72  # Arc extent to match the pentagon's angle

# Draw the pentagons in a circular formation
for i in range(num_pentagons):
    draw_pentagon(pentagon_side)
    t.penup()
    t.forward(pentagon_side)
    t.right(angle_between_pentagons)
    t.pendown()

# Draw the inward-facing arcs
t.penup()
t.goto(0, 0)
t.setheading(0)
t.pendown()

for i in range(num_pentagons):
    t.penup()
    t.forward(pentagon_side)
    t.right(36)
    t.pendown()
    draw_arc(arc_radius, arc_extent)
    t.penup()
    t.goto(0, 0)
    t.setheading((i + 1) * angle_between_pentagons)
    t.pendown()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()