import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.speed(1)
drawer.pensize(3)
drawer.color("black")

# Function to draw a circle
def draw_circle():
    drawer.penup()
    drawer.goto(-150, 0)  # Position the turtle to the left side of the canvas
    drawer.pendown()
    drawer.circle(50)  # Draw a circle with radius 50

# Function to draw a line
def draw_line():
    drawer.penup()
    drawer.goto(50, 0)  # Position the turtle to the right side of the canvas
    drawer.pendown()
    drawer.forward(100)  # Draw a horizontal line

# Draw the circle
draw_circle()

# Draw the line
draw_line()

# Hide the turtle and display the window
drawer.hideturtle()
screen.mainloop()