import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.pensize(2)  # Set the pen size for the outline

# Function to draw a line
def draw_line(angle, length):
    t.setheading(angle)
    t.forward(length)

# Function to draw a circle with a black border
def draw_circle(radius):
    t.pendown()
    t.circle(radius)
    t.penup()

# Move to the starting point
t.penup()
t.goto(0, 0)
t.pendown()

# Draw the Y-shaped structure
line_length = 100
circle_radius = 20

# Draw the first line and circle
draw_line(90, line_length)
draw_circle(circle_radius)

# Draw the second line and circle
t.goto(0, 0)
draw_line(210, line_length)
draw_circle(circle_radius)

# Draw the third line and circle
t.goto(0, 0)
draw_line(330, line_length)
draw_circle(circle_radius)

# Hide the turtle and finish
t.hideturtle()
screen.mainloop()