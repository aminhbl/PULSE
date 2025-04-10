import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(1)  # Set the speed of the turtle
t.penup()
t.goto(-200, -200)  # Start at the bottom left corner
t.pendown()

# Define the step size
step_size = 50

# Draw the staircase
for _ in range(3):
    t.forward(step_size)  # Draw horizontal line
    t.left(90)  # Turn left
    t.forward(step_size)  # Draw vertical line
    t.right(90)  # Turn right

# Hide the turtle and display the window
t.hideturtle()
turtle.done()