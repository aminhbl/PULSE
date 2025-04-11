import turtle
import math

# Function to draw a line
def draw_line(t, length):
    t.forward(length)

# Function to draw a heptagon
def draw_heptagon(t, side_length):
    for _ in range(7):
        t.forward(side_length)
        t.right(360 / 7)

# Setup the turtle
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.color("black")
t.speed(0)  # Fastest speed
t.penup()

# Constants
num_lines = 6
line_length = 100
heptagon_side_length = 50
angle_between_lines = 360 / num_lines
heptagon_angle_offset = 90 - (360 / 7) / 2  # To make one side perpendicular to the line

# Draw the star-like pattern with heptagons
for i in range(num_lines):
    t.goto(0, 0)
    t.setheading(angle_between_lines * i)
    t.pendown()
    draw_line(t, line_length)
    t.penup()
    
    # Move to the end of the line to draw the heptagon
    t.forward(heptagon_side_length / 2)
    t.right(heptagon_angle_offset)
    t.pendown()
    draw_heptagon(t, heptagon_side_length)
    t.penup()

# Hide the turtle and display the result
t.hideturtle()
screen.mainloop()