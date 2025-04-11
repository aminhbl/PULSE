import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Square and Semicircle with Connecting Line")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.speed(1)

# Function to draw a square
def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Function to draw a semicircle
def draw_semicircle(t, radius):
    t.circle(radius, 180)

# Draw the square
drawer.penup()
drawer.goto(-150, 0)
drawer.pendown()
draw_square(drawer, 100)

# Draw the semicircle
drawer.penup()
drawer.goto(50, 0)
drawer.setheading(90)  # Point upwards
drawer.pendown()
draw_semicircle(drawer, 50)

# Draw the connecting line
drawer.penup()
drawer.goto(-150, 100)
drawer.pendown()
drawer.forward(300)

# Hide the turtle
drawer.hideturtle()

# Finish
screen.mainloop()