import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(1)

# Draw a long horizontal line
t.penup()
t.goto(-200, 0)
t.pendown()
t.forward(400)

# Draw a semi-circle at the end of the line
t.left(90)
t.circle(50, 180)  # Draw a semi-circle with radius 50

# Hide the turtle and display the window
t.hideturtle()
turtle.done()