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
        t.left(90)

# Function to draw the pinwheel pattern
def draw_pinwheel(size):
    for _ in range(3):
        draw_square(size)
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.right(90)

# Move the turtle to the starting position
t.penup()
t.goto(-50, -50)
t.pendown()

# Draw the pinwheel pattern
draw_pinwheel(100)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()