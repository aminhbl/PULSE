import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
snowflake_turtle = turtle.Turtle()
snowflake_turtle.color("black")
snowflake_turtle.speed(0)  # Fastest drawing speed

# Function to draw a line
def draw_line(length):
    snowflake_turtle.forward(length)

# Function to draw a circle
def draw_circle(radius):
    snowflake_turtle.circle(radius)

# Function to draw a snowflake arm
def draw_snowflake_arm():
    # Leave a short space
    snowflake_turtle.penup()
    snowflake_turtle.forward(20)
    snowflake_turtle.pendown()
    
    # Draw a short line
    draw_line(30)
    
    # Leave another short space
    snowflake_turtle.penup()
    snowflake_turtle.forward(20)
    snowflake_turtle.pendown()
    
    # Draw a large circle at the end of the arm
    draw_circle(20)

# Number of arms
num_arms = 7
angle_between_arms = 360 / num_arms

# Draw the snowflake
for _ in range(num_arms):
    draw_snowflake_arm()
    snowflake_turtle.penup()
    snowflake_turtle.goto(0, 0)
    snowflake_turtle.pendown()
    snowflake_turtle.right(angle_between_arms)

# Hide the turtle and display the result
snowflake_turtle.hideturtle()
screen.mainloop()