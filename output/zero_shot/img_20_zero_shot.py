import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.speed(0)
drawer.pensize(3)

# Function to draw a regular nonagon
def draw_nonagon(size):
    for _ in range(9):
        drawer.forward(size)
        drawer.left(40)

# Function to draw a semicircle
def draw_semicircle(radius):
    drawer.circle(radius, 180)

# Draw the nonagon
drawer.penup()
drawer.goto(-150, 0)
drawer.pendown()
drawer.color("black")
draw_nonagon(100)

# Draw the semicircle
drawer.penup()
drawer.goto(50, 100)  # Position slightly above the top right side of the nonagon
drawer.setheading(-45)  # Rotate to the right
drawer.pendown()
draw_semicircle(50)

# Hide the turtle and finish
drawer.hideturtle()
screen.mainloop()