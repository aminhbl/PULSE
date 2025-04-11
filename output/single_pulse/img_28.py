import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.speed(1)
drawer.pensize(3)  # Set the pen size for bold lines
drawer.color("black")

# Function to draw a pentagon
def draw_pentagon():
    for _ in range(5):
        drawer.forward(100)
        drawer.right(72)

# Function to draw a circle
def draw_circle():
    drawer.circle(50)

# Draw the pentagon on the left side
drawer.penup()
drawer.goto(-150, 0)  # Position the turtle for the pentagon
drawer.pendown()
draw_pentagon()

# Draw the circle on the right side
drawer.penup()
drawer.goto(100, -50)  # Position the turtle for the circle
drawer.pendown()
draw_circle()

# Draw the connecting line
drawer.penup()
drawer.goto(-150, 0)  # Start at the base of the pentagon
drawer.pendown()
drawer.goto(50, 0)  # End at the base of the circle

# Hide the turtle and finish
drawer.hideturtle()
screen.mainloop()