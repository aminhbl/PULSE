import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.speed(0)

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Function to position the turtle
def move_to_position(angle, distance):
    t.penup()
    t.setheading(angle)
    t.forward(distance)
    t.pendown()

# Parameters
square_size = 30
circle_radius = 60
num_squares = 8

# Draw squares in a circular pattern
for i in range(num_squares):
    angle = i * (360 / num_squares)
    move_to_position(angle, circle_radius)
    draw_square(square_size)
    move_to_position(angle + 180, circle_radius)  # Move back to center

# Hide the turtle and finish
t.hideturtle()
screen.mainloop()