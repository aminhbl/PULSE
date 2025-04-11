import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(1)  # Slow down the turtle for better visualization
t.penup()
t.goto(-200, -200)  # Start at the bottom left corner
t.pendown()

# Define the step size
step_size = 100

# Draw the staircase pattern
for _ in range(6):
    # Draw horizontal line
    t.forward(step_size)
    # Draw vertical line
    t.left(90)
    t.forward(step_size)
    t.right(90)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()