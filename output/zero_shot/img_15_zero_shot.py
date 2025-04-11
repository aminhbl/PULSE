import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(1)
t.pensize(3)

# Function to draw a regular pentagon
def draw_pentagon(side_length):
    for _ in range(5):
        t.forward(side_length)
        t.right(72)

# Function to draw a square
def draw_square(side_length):
    for _ in range(4):
        t.forward(side_length)
        t.right(90)

# Draw the pentagon
t.penup()
t.goto(-150, 0)  # Position the turtle to the left
t.pendown()
draw_pentagon(100)

# Draw the square
t.penup()
t.goto(50, 0)  # Position the turtle to the right with some space
t.pendown()
draw_square(100)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()