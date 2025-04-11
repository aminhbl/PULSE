import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.speed(0)
drawer.pensize(2)

# Function to draw a square
def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Function to draw a semi-circle
def draw_semi_circle(t, radius):
    t.circle(radius, 180)

# Function to draw a line
def draw_line(t, length):
    t.forward(length)

# Draw the square on the left side
drawer.penup()
drawer.goto(-200, 0)
drawer.pendown()
draw_square(drawer, 100)

# Draw the semi-circle on the right side
drawer.penup()
drawer.goto(100, 0)
drawer.setheading(90)
drawer.pendown()
draw_semi_circle(drawer, 50)

# Draw the horizontal line connecting the top of the square and the semi-circle
drawer.penup()
drawer.goto(-200, 100)
drawer.setheading(0)
drawer.pendown()
draw_line(drawer, 300)

# Hide the turtle
drawer.hideturtle()

# Finish
turtle.done()