import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.penup()

# Constants
num_lines = 5
line_length = 100
circle_radius = 10
gap_from_center = 20
gap_to_circle = 10

# Function to draw a line
def draw_line(angle):
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(gap_from_center)
    t.pendown()
    t.forward(line_length - gap_to_circle)
    t.penup()

# Function to draw a circle at the end of a line
def draw_circle(angle):
    t.setheading(angle)
    t.forward(line_length)
    t.pendown()
    t.circle(circle_radius)
    t.penup()

# Draw the snowflake
for i in range(num_lines):
    angle = i * (360 / num_lines)
    draw_line(angle)
    draw_circle(angle)

# Hide the turtle and display the result
t.hideturtle()
screen.mainloop()