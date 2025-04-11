import turtle

# Function to draw a square
def draw_square(t, size):
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.penup()

# Function to draw a hexagon
def draw_hexagon(t, size):
    t.pendown()
    for _ in range(6):
        t.forward(size)
        t.right(60)
    t.penup()

# Setup the screen
screen = turtle.Screen()
screen.setup(width=800, height=400)

# Create a turtle for drawing
t = turtle.Turtle()
t.speed(0)
t.pensize(3)
t.penup()

# Draw the square on the left side
t.goto(-200, 0)  # Position the turtle to the left
draw_square(t, 100)

# Draw the hexagon on the right side
t.goto(100, 0)  # Position the turtle to the right
draw_hexagon(t, 100)

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()