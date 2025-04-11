import turtle

# Set up the turtle
t = turtle.Turtle()
t.pensize(3)  # Bold lines
t.speed(1)    # Slow speed for drawing

# Draw a square on the left
t.penup()
t.goto(-150, 0)  # Move to the starting position for the square
t.pendown()
for _ in range(4):
    t.forward(100)
    t.right(90)

# Draw a triangle on the right
t.penup()
t.goto(50, 0)  # Move to the starting position for the triangle
t.pendown()
for _ in range(3):
    t.forward(100)
    t.left(120)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()