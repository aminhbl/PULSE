import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Function to draw a triangle
def draw_triangle(t, size):
    t.pendown()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.penup()

# Function to draw an octagon
def draw_octagon(t, size):
    t.pendown()
    for _ in range(8):
        t.forward(size)
        t.left(45)
    t.penup()

# Function to draw a bold line
def draw_bold_line(t, length):
    t.pensize(3)
    t.pendown()
    t.forward(length)
    t.penup()

# Create a turtle for drawing
t = turtle.Turtle()
t.color("black")
t.speed(1)
t.penup()

# Draw the triangle on the left
t.goto(-200, 0)
draw_triangle(t, 50)

# Draw the octagon on the right
t.goto(100, 0)
draw_octagon(t, 50)

# Draw the bold line connecting the base of the triangle and the octagon
t.goto(-200, 0)
draw_bold_line(t, 300)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()