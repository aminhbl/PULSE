import turtle
import math

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")

# Function to draw a single arm of the snowflake
def draw_arm():
    t.penup()
    t.forward(20)  # Move forward to start the arm, leaving a gap
    t.pendown()
    t.forward(50)  # Draw the line of the arm
    t.penup()
    t.forward(10)  # Move forward to start the square
    t.pendown()
    for _ in range(4):  # Draw a square
        t.forward(20)
        t.right(90)
    t.penup()
    t.backward(80)  # Move back to the center
    t.pendown()

# Draw the seven-armed snowflake
for i in range(7):
    draw_arm()
    t.right(360 / 7)  # Evenly space the arms

# Hide the turtle and display the window
t.hideturtle()
turtle.done()