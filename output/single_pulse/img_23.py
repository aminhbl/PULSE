import turtle

# Function to draw a square
def draw_square(t, size):
    t.pensize(3)
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.penup()

# Function to draw a triangle
def draw_triangle(t, size):
    t.pensize(3)
    t.pendown()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.penup()

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
t = turtle.Turtle()
t.color("black")
t.speed(1)
t.penup()

# Draw the square on the left side
t.goto(-150, 0)  # Position the turtle to the left
draw_square(t, 100)

# Draw the triangle on the right side
t.goto(50, 0)  # Position the turtle to the right
draw_triangle(t, 100)

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()