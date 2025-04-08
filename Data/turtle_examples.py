# Using python turtle write a python program to Draw a Circle with a solid border.

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
my_turtle = turtle.Turtle()
my_turtle.pensize(3)            # Set the border thickness
my_turtle.color("black")        # Use black color for the border
my_turtle.speed(1)

# Draw the circle with no fill
my_turtle.circle(100)           # Radius of the circle

# Wait for user click to close the window
screen.exitonclick()

