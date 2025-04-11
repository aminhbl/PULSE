import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(1)  # Set the speed of the turtle

# Draw the long horizontal line
t.penup()
t.goto(-200, 0)  # Start from the left side of the screen
t.pendown()
t.forward(200)  # Draw the horizontal line

# Draw the semicircle
t.left(90)  # Turn the turtle upwards
t.circle(100, 180)  # Draw a semicircle with radius 100

# Hide the turtle and display the window
t.hideturtle()
turtle.done()