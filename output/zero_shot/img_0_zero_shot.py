import turtle

def draw_square_spiral():
    # Set up the turtle
    wn = turtle.Screen()
    wn.bgcolor("white")
    spiral_turtle = turtle.Turtle()
    spiral_turtle.speed(0)  # Fastest speed

    # Initial parameters
    length = 10
    increment = 10
    angle = 90

    # Draw the square spiral
    for _ in range(20):  # Adjust the range for more or fewer turns
        spiral_turtle.forward(length)
        spiral_turtle.right(angle)
        length += increment

    # Draw the vertical line from the top-left corner
    spiral_turtle.right(90)
    spiral_turtle.forward(length)

    # Hide the turtle and finish
    spiral_turtle.hideturtle()
    wn.mainloop()

draw_square_spiral()