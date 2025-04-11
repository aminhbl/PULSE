import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(1)

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Function to draw a hexagon
def draw_hexagon(size):
    for _ in range(6):
        t.forward(size)
        t.right(60)

# Draw the square
square_size = 50
t.penup()
t.goto(-100, 0)
t.pendown()
draw_square(square_size)

# Draw the hexagon
hexagon_size = 50
t.penup()
t.goto(0, 0)
t.pendown()
draw_hexagon(hexagon_size)

# Draw the connecting line
t.penup()
t.goto(-100, -square_size)
t.pendown()
t.forward(100)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()