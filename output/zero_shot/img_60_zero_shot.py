import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")

# Number of lines
num_lines = 7

# Draw the starburst
for i in range(num_lines):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.forward(100)
    t.backward(100)
    t.right(360 / num_lines)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()