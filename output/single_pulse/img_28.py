import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(3)

# Function to draw a pentagon
def draw_pentagon():
    for _ in range(5):
        t.forward(100)
        t.right(72)

# Function to draw a circle
def draw_circle():
    t.circle(50)

# Function to draw a line
def draw_line(length):
    t.forward(length)

# Draw the pentagon
t.penup()
t.goto(-200, 0)
t.pendown()
draw_pentagon()

# Draw the circle
t.penup()
t.goto(100, -50)  # Adjusted to align the base of the circle with the pentagon
t.pendown()
draw_circle()

# Draw the connecting line
t.penup()
t.goto(-100, -50)  # Start from the base of the pentagon
t.pendown()
draw_line(200)  # Length to connect the base of the pentagon to the base of the circle

# Hide the turtle and display the window
t.hideturtle()
turtle.done()