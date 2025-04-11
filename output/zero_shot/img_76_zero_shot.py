import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.penup()

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Parameters
num_squares = 6
square_size = 50
angle_between_squares = 360 / num_squares
rotation_angle = 15  # Rotation for each square

# Draw squares in a circular pattern
for i in range(num_squares):
    # Calculate the position for each square
    angle = math.radians(angle_between_squares * i)
    x = 100 * math.cos(angle)
    y = 100 * math.sin(angle)
    
    # Move to the starting position
    t.goto(x, y)
    t.setheading(angle_between_squares * i + rotation_angle * i)
    
    # Draw the square
    t.pendown()
    draw_square(square_size)
    t.penup()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()