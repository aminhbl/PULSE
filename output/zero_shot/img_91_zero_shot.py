import turtle
import math

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")
t.color("blue")

# Function to draw a single arm of the snowflake
def draw_arm():
    t.penup()
    t.forward(50)  # Move forward to start the arm
    t.pendown()
    t.forward(100)  # Draw the line part of the arm
    t.penup()
    t.forward(20)  # Gap before the semicircle
    t.pendown()
    t.circle(20, 180)  # Draw a semicircle
    t.penup()
    t.backward(170)  # Return to the center
    t.pendown()

# Draw the seven-armed snowflake
for _ in range(7):
    draw_arm()
    t.right(360 / 7)  # Evenly space the arms

# Hide the turtle and display the window
t.hideturtle()
turtle.done()