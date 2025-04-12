import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
snowflake = turtle.Turtle()
snowflake.speed(0)  # Fastest speed

# Function to draw a single arm of the snowflake
def draw_arm():
    snowflake.penup()
    snowflake.forward(50)  # Move forward to start the arm
    snowflake.pendown()
    snowflake.forward(50)  # Draw the line part of the arm
    snowflake.penup()
    snowflake.forward(10)  # Gap before the semicircle
    snowflake.pendown()
    snowflake.circle(10, 180)  # Draw a semicircle
    snowflake.penup()
    snowflake.backward(110)  # Return to the center
    snowflake.pendown()

# Draw the eight-armed snowflake
for _ in range(8):
    draw_arm()
    snowflake.right(45)  # Rotate to the next arm position

# Hide the turtle and display the window
snowflake.hideturtle()
screen.mainloop()