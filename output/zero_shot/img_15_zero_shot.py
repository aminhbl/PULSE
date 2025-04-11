import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Pentagon and Square")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.pensize(3)  # Bold lines
drawer.speed(1)

# Function to draw a regular pentagon
def draw_pentagon(side_length):
    for _ in range(5):
        drawer.forward(side_length)
        drawer.right(72)

# Function to draw a square
def draw_square(side_length):
    for _ in range(4):
        drawer.forward(side_length)
        drawer.right(90)

# Draw the pentagon
drawer.penup()
drawer.goto(-150, 0)  # Position the turtle to the left
drawer.pendown()
draw_pentagon(100)

# Draw the square
drawer.penup()
drawer.goto(50, 0)  # Position the turtle to the right with some space
drawer.pendown()
draw_square(100)

# Hide the turtle and finish
drawer.hideturtle()
screen.mainloop()