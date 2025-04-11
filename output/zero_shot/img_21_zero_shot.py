import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(1)
t.pensize(3)  # Bold lines

# Draw a small square on the left
t.penup()
t.goto(-150, 0)  # Move to the starting position for the square
t.pendown()
for _ in range(4):
    t.forward(50)
    t.right(90)

# Draw a regular hexagon on the right
t.penup()
t.goto(50, 0)  # Move to the starting position for the hexagon
t.pendown()
for _ in range(6):
    t.forward(50)
    t.right(60)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()