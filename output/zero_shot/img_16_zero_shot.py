import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Octagon and Semicircle")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.pensize(3)  # Bold lines
drawer.speed(1)

# Function to draw a regular octagon
def draw_octagon(size):
    for _ in range(8):
        drawer.forward(size)
        drawer.left(45)

# Function to draw a semicircle
def draw_semicircle(radius):
    drawer.circle(radius, 180)

# Draw the octagon on the left
drawer.penup()
drawer.goto(-150, 0)  # Position the turtle to the left
drawer.pendown()
draw_octagon(50)

# Draw the semicircle on the right
drawer.penup()
drawer.goto(100, 0)  # Position the turtle to the right
drawer.setheading(90)  # Face upwards to start the semicircle
drawer.pendown()
draw_semicircle(50)

# Hide the turtle and finish
drawer.hideturtle()
screen.mainloop()