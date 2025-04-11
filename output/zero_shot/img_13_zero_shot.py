import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(1)  # Set the speed of the turtle

# Define the length of each step
step_length = 50

# Draw the staircase pattern
for _ in range(6):
    t.forward(step_length)  # Draw horizontal line
    t.left(90)             # Turn left 90 degrees
    t.forward(step_length)  # Draw vertical line
    t.right(90)            # Turn right 90 degrees

# Hide the turtle and display the window
t.hideturtle()
turtle.done()