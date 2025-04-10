import turtle

# Setup the turtle
t = turtle.Turtle()
t.speed(3)  # Moderate speed
t.pensize(2)

# Starting length of the first square
side_length = 20
# How much each square increases in size
increment = 20

# Draw 8 squares
for i in range(8):
    for _ in range(4):
        t.forward(side_length)
        t.right(90)
    # Move to new starting position (bottom-left of next larger square)
    t.penup()
    t.backward(increment)
    t.right(90)
    t.forward(increment)
    t.left(90)
    t.pendown()
    # Increase side length for the next square
    side_length += increment

# Finish
turtle.done()
