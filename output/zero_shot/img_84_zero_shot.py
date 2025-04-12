import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Parameters
num_squares = 8
small_square_size = 30
radius = 100
angle_between_squares = 360 / num_squares

# Draw squares in a circular pattern
for i in range(num_squares):
    # Calculate the angle for the current square
    angle = i * angle_between_squares
    
    # Move to the starting position for the current square
    t.penup()
    t.goto(radius * math.cos(math.radians(angle)), radius * math.sin(math.radians(angle)))
    t.setheading(angle + 45)  # Rotate the square slightly
    t.pendown()
    
    # Draw the square
    draw_square(small_square_size)

# Hide the turtle and display the result
t.hideturtle()
screen.mainloop()