import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")

# Draw the asterisk-like shape
for _ in range(8):
    t.forward(100)  # Draw a line
    t.backward(100)  # Return to the center
    t.right(45)  # Rotate 45 degrees for the next line

# Hide the turtle and display the window
t.hideturtle()
turtle.done()