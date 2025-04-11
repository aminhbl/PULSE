import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(1)  # Set the speed of the turtle
t.penup()
t.goto(-200, -200)  # Start at the bottom left corner
t.pendown()

# Define the length of each step
step_length = 50

# Draw the staircase
for _ in range(8):
    t.forward(step_length)  # Draw horizontal line
    t.left(90)  # Turn left to draw vertical line
    t.forward(step_length)  # Draw vertical line
    t.right(90)  # Turn right to prepare for next horizontal line

# Hide the turtle and display the window
t.hideturtle()
turtle.done()