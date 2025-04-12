import turtle
import math

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")
t.color("black")

# Function to draw a line
def draw_line(length):
    t.penup()
    t.forward(length)
    t.pendown()
    t.forward(20)  # Draw the line with a small gap at the start

# Function to draw a square centered at the current position
def draw_square(size):
    t.penup()
    t.forward(size / 2)
    t.right(90)
    t.forward(size / 2)
    t.right(90)
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.penup()
    t.left(90)
    t.forward(size / 2)
    t.left(90)
    t.forward(size / 2)
    t.left(180)

# Main function to draw the snowflake pattern
def draw_snowflake():
    num_arms = 7
    arm_length = 100
    square_size = 20
    angle = 360 / num_arms

    for _ in range(num_arms):
        t.penup()
        t.goto(0, 0)
        t.setheading(0)
        t.left(angle * _)
        draw_line(arm_length)
        draw_square(square_size)

# Draw the snowflake
draw_snowflake()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()