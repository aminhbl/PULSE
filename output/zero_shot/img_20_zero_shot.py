import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.speed(1)
drawer.pensize(3)  # Bold lines

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
drawer.goto(-150, 0)  # Position the nonagon on the left
drawer.pendown()
draw_nonagon(100)

# Draw the semicircle
drawer.penup()
drawer.goto(50, 100)  # Position the semicircle slightly above the nonagon
drawer.setheading(180)  # Face the semicircle to the left
drawer.pendown()
draw_semicircle(50)

# Hide the turtle and display the window
drawer.hideturtle()
screen.mainloop()