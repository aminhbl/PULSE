import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")

# Define the central point
central_x, central_y = 0, 0
t.penup()
t.goto(central_x, central_y)
t.pendown()

# Define the number of lines and the angle between them
num_lines = 7
angle = 360 / num_lines
line_length = 100  # Length of each line

# Draw the lines
for _ in range(num_lines):
    t.forward(line_length)
    t.penup()
    t.goto(central_x, central_y)
    t.pendown()
    t.right(angle)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()