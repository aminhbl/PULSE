import turtle
import math

# Function to draw a square
def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.color("black")
t.speed(0)  # Fastest speed

# Central point of the canvas
center_x, center_y = 0, 0

# Radius of the circle
radius = 100

# Size of each square
square_size = 50

# Number of squares
num_squares = 8

# Angle between each square
angle_between_squares = 360 / num_squares

# Draw the squares
for i in range(num_squares):
    # Calculate the angle for the current square
    angle = math.radians(i * angle_between_squares)
    
    # Calculate the position of the center of the square
    square_center_x = center_x + radius * math.cos(angle)
    square_center_y = center_y + radius * math.sin(angle)
    
    # Move the turtle to the starting position of the square
    t.penup()
    t.goto(square_center_x - square_size / 2, square_center_y - square_size / 2)
    t.pendown()
    
    # Rotate the turtle to face the correct direction
    t.setheading(i * angle_between_squares)
    
    # Draw the square
    draw_square(t, square_size)

# Hide the turtle and display the result
t.hideturtle()
screen.mainloop()