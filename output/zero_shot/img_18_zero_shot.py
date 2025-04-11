import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Circle and Nonagon")
screen.bgcolor("white")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.speed(0)
drawer.pensize(3)  # Bold lines
drawer.color("black")

# Function to draw a circle
def draw_circle(radius):
    drawer.penup()
    drawer.goto(-150, 0)  # Position for the circle
    drawer.pendown()
    drawer.circle(radius)

# Function to draw a regular nonagon
def draw_nonagon(side_length):
    drawer.penup()
    drawer.goto(50, 0)  # Position for the nonagon
    drawer.pendown()
    for _ in range(9):
        drawer.forward(side_length)
        drawer.left(40)

# Draw the circle
draw_circle(50)

# Draw the nonagon
draw_nonagon(40)

# Hide the turtle and finish
drawer.hideturtle()
screen.mainloop()