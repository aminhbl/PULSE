import turtle

def draw_nonagon(side_length):
    # Set up the turtle
    turtle.bgcolor("white")
    turtle.color("black")
    turtle.speed(1)  # Slow speed for drawing
    turtle.penup()
    turtle.goto(-side_length / 2, 0)  # Start at the left edge of the nonagon
    turtle.pendown()

    # Draw a nonagon
    for _ in range(9):
        turtle.forward(side_length)
        turtle.left(40)  # 360/9 = 40 degrees

    # Hide the turtle and finish
    turtle.hideturtle()
    turtle.done()

# Set the side length for the nonagon
side_length = 100

# Call the function to draw the nonagon
draw_nonagon(side_length)