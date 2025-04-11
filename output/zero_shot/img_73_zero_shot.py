import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed

# Function to draw a triangle
def draw_triangle(side_length):
    for _ in range(3):
        t.forward(side_length)
        t.left(120)

# Function to draw the pattern
def draw_pattern():
    num_triangles = 8
    side_length = 100
    angle_between = 360 / num_triangles
    radius = side_length / (2 * math.sin(math.radians(180 / num_triangles)))

    for _ in range(num_triangles):
        # Move to the starting point of the triangle
        t.penup()
        t.goto(0, 0)
        t.forward(radius)
        t.pendown()

        # Draw the triangle
        draw_triangle(side_length)

        # Draw the line from the center to the base midpoint
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.forward(radius)

        # Rotate to the next position
        t.left(angle_between)

# Draw the pattern
draw_pattern()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()