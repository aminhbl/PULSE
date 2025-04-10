import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
triangle_turtle = turtle.Turtle()
triangle_turtle.color("black")
triangle_turtle.pensize(2)

# Define the side length of the triangle
side_length = 100

# Draw an equilateral triangle
for _ in range(3):
    triangle_turtle.forward(side_length)
    triangle_turtle.left(120)

# Hide the turtle and finish
triangle_turtle.hideturtle()
turtle.done()