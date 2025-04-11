import turtle

# Function to draw a line
def draw_line(t, length):
    t.forward(length)

# Function to draw a square
def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Setup the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")
t.color("black")

# Constants
num_arms = 7
arm_length = 100
line_segment_length = 20
space_between_segments = 10
square_size = 20
angle_between_arms = 360 / num_arms

# Draw the snowflake pattern
for i in range(num_arms):
    t.penup()
    t.goto(0, 0)
    t.setheading(angle_between_arms * i)
    t.pendown()
    
    # Draw the line segment
    t.forward(space_between_segments)
    draw_line(t, line_segment_length)
    
    # Move to the end of the arm
    t.penup()
    t.forward(arm_length - line_segment_length - space_between_segments)
    
    # Draw the square
    t.pendown()
    t.right(45)  # Rotate the square for radial symmetry
    draw_square(t, square_size)
    t.left(45)  # Reset the rotation for the next arm

# Hide the turtle and display the window
t.hideturtle()
turtle.done()