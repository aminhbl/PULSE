import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(1)

# Draw a circle on the left side of the canvas
t.penup()
t.goto(-100, 0)
t.pendown()
t.circle(50)

# Draw a straight horizontal line starting from the top of the circle
t.penup()
t.goto(-100, 50)
t.pendown()
t.forward(200)

# Draw a semi-circle at the end of the line
t.right(90)
t.circle(50, 180)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()