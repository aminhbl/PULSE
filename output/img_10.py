import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(1)  # Set the speed of the turtle
t.penup()
t.goto(-200, -200)  # Start at the bottom left corner
t.pendown()

# Define the length of each step
step_length = 100

# Draw the staircase
for _ in range(5):
    # Draw horizontal line
    t.forward(step_length)
    # Draw vertical line
    t.left(90)
    t.forward(step_length)
    t.right(90)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()