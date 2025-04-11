import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)

# Function to draw a square
def draw_square(side_length):
    for _ in range(4):
        t.forward(side_length)
        t.right(90)

# Function to draw a hexagon
def draw_hexagon(side_length):
    for _ in range(6):
        t.forward(side_length)
        t.right(60)

# Draw the square on the left side
t.penup()
t.goto(-150, 0)  # Position the turtle to the left side
t.pendown()
draw_square(100)

# Draw the hexagon on the right side
t.penup()
t.goto(50, 0)  # Position the turtle to the right side
t.pendown()
draw_hexagon(100)

# Draw the connecting line
t.penup()
t.goto(-150, -100)  # Move to the bottom left corner of the square
t.pendown()
t.forward(300)  # Draw a line to the bottom right corner of the hexagon

# Hide the turtle and display the window
t.hideturtle()
turtle.done()