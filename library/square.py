import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.color("black")
drawer.pensize(2)

# Function to draw a square
def draw_square(side_length):
    for _ in range(4):
        drawer.forward(side_length)
        drawer.right(90)

# Draw a square with a side length of 100 units
draw_square(100)

# Hide the turtle and finish
drawer.hideturtle()
screen.mainloop()