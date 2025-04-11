import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(1)
t.pensize(3)  # Bold black lines

# Function to draw a triangle
def draw_triangle():
    for _ in range(3):
        t.forward(50)
        t.left(120)

# Function to draw a regular octagon
def draw_octagon():
    for _ in range(8):
        t.forward(50)
        t.left(45)

# Draw the triangle
t.penup()
t.goto(-150, 0)
t.pendown()
draw_triangle()

# Draw the connecting line
t.penup()
t.goto(-100, 0)
t.pendown()
t.forward(200)

# Draw the octagon
t.penup()
t.goto(100, 0)
t.pendown()
draw_octagon()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()