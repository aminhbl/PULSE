import turtle
import math

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")

# Function to draw an arc
def draw_arc(radius, extent):
    t.circle(radius, extent)

# Number of arcs
num_arcs = 8
angle_between_arcs = 360 / num_arcs
arc_radius = 100
arc_extent = 60  # Extent of each arc

# Draw the pattern
for _ in range(num_arcs):
    draw_arc(arc_radius, arc_extent)
    t.left(angle_between_arcs)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()