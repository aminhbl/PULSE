import turtle

# Setup turtle
t = turtle.Turtle()
t.speed(3)
t.pensize(2)

# Initial side length
side_length = 30
# How much to increase each square
increment = 20

# Draw 6 stacked, spiraling squares
for i in range(6):
    # Draw the square
    for _ in range(4):
        t.forward(side_length)
        t.right(90)
    
    # Move to new position: bottom-left corner of next square
    t.penup()
    t.backward(increment)
    t.right(90)
    t.forward(increment)
    t.left(90)
    t.pendown()
    
    # Increase size
    side_length += increment

turtle.done()
