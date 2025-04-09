# Using python turtle write a python program to Draw a triangle next to a square with a solid border.

import turtle

# Set up the turtle
t = turtle.Turtle()
t.pensize(3)  # Solid border width
t.speed(3)

# Draw square
square_size = 100
t.penup()
t.goto(-150, 0)  # Start position for square
t.pendown()
for _ in range(4):
    t.forward(square_size)
    t.right(90)

# Draw triangle next to the square
triangle_size = 100
t.penup()
t.goto(-150 + square_size + 20, 0)  # Move right of the square
t.pendown()
for _ in range(3):
    t.forward(triangle_size)
    t.left(120)

# Finish
turtle.done()

# ----------- ---------------- ------------------ --------------- ---------------- 

# Using python turtle write a python program to Draw a Circle with a solid border.

# import turtle

# # Set up the screen
# screen = turtle.Screen()
# screen.bgcolor("white")

# # Create turtle
# my_turtle = turtle.Turtle()
# my_turtle.pensize(3)            # Set the border thickness
# my_turtle.color("black")        # Use black color for the border
# my_turtle.speed(1)

# # Draw the circle with no fill
# my_turtle.circle(100)           # Radius of the circle

# # Wait for user click to close the window
# screen.exitonclick()

