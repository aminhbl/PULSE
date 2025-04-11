import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.speed(1)
drawer.pensize(3)

# Function to draw a heptagon
def draw_heptagon(size):
    for _ in range(7):
        drawer.forward(size)
        drawer.left(360 / 7)

# Function to draw a circle
def draw_circle(radius):
    drawer.circle(radius)

# Draw the heptagon
drawer.penup()
drawer.goto(-150, 0)  # Position for the heptagon
drawer.pendown()
drawer.color("black")
draw_heptagon(50)

# Draw the circle
drawer.penup()
drawer.goto(100, -25)  # Position for the circle
drawer.pendown()
drawer.color("black")
draw_circle(25)

# Hide the turtle and display the window
drawer.hideturtle()
turtle.done()