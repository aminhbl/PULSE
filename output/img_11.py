import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(1)  # You can adjust the speed; 1 is slowest, 10 is fastest
t.penup()
t.goto(-200, -200)  # Start at the bottom left corner
t.pendown()

# Define the length of each step
step_length = 50

# Draw the staircase pattern
for _ in range(7):
    # Draw horizontal line
    t.forward(step_length)
    # Draw vertical line
    t.left(90)
    t.forward(step_length)
    t.right(90)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()