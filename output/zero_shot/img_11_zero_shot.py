import turtle

def draw_staircase(steps, step_length):
    for _ in range(steps):
        turtle.forward(step_length)
        turtle.left(90)
        turtle.forward(step_length)
        turtle.right(90)

# Set up the turtle
turtle.speed(1)
turtle.penup()
turtle.goto(-200, -200)  # Start from bottom left
turtle.pendown()

# Draw the staircase
draw_staircase(8, 50)

# Hide the turtle and display the window
turtle.hideturtle()
turtle.done()