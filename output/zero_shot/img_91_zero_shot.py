import turtle
import math

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")

# Function to draw a single arm of the snowflake
def draw_arm():
    t.penup()
    t.forward(20)  # Short space
    t.pendown()
    t.forward(20)  # Short line
    t.penup()
    t.forward(20)  # Another short space
    t.pendown()
    t.left(90)  # Prepare to draw the semicircle
    t.circle(20, 180)  # Draw a semicircle
    t.left(90)  # Reorient back to the original direction

# Draw the seven-sided snowflake pattern
for _ in range(7):
    draw_arm()
    t.penup()
    t.goto(0, 0)  # Return to the center
    t.pendown()
    t.right(360 / 7)  # Rotate to the next arm

# Hide the turtle and display the window
t.hideturtle()
turtle.done()