import turtle

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
line_turtle = turtle.Turtle()
line_turtle.color("black")
line_turtle.penup()  # Lift the pen to move without drawing
line_turtle.goto(-100, 0)  # Move to the starting point of the line
line_turtle.pendown()  # Lower the pen to start drawing

# Draw a line
line_turtle.forward(200)  # Draw a line 200 units long

# Hide the turtle and finish
line_turtle.hideturtle()
turtle.done()