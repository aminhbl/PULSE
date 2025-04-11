import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(1)
t.pensize(3)  # Bold lines
t.penup()
t.goto(-200, 0)  # Starting position
t.pendown()

# Function to draw a single triangle
def draw_triangle():
    for _ in range(3):
        t.forward(100)
        t.left(120)

# Draw four triangles side by side
for _ in range(4):
    draw_triangle()
    t.forward(100)  # Move to the start of the next triangle

# Hide the turtle and display the window
t.hideturtle()
turtle.done()