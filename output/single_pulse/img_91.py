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
    t.forward(10)  # Small gap before the semicircle
    t.penup()
    t.backward(length + 10)

# Function to draw a semicircle
def draw_semi_circle(radius):
    t.penup()
    t.forward(radius)
    t.pendown()
    t.left(90)
    t.circle(radius, 180)
    t.left(90)
    t.penup()
    t.backward(radius)

# Main function to draw the snowflake pattern
def draw_snowflake():
    num_arms = 7
    arm_length = 100
    semi_circle_radius = 20
    angle_between_arms = 360 / num_arms

    for _ in range(num_arms):
        t.penup()
        t.goto(0, 0)
        t.setheading(0)
        t.left(angle_between_arms * _)
        t.forward(20)  # Small space from the center
        draw_line(arm_length)
        draw_semi_circle(semi_circle_radius)

# Draw the snowflake
draw_snowflake()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()