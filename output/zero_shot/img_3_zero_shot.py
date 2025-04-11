import turtle

def draw_spiral_squares():
    # Set up the turtle
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.penup()
    t.goto(0, 0)
    t.pendown()

    # Initial size of the smallest square
    size = 20

    # Draw 8 squares
    for i in range(8):
        for _ in range(4):
            t.forward(size)
            t.left(90)
        # Move to the next starting point
        t.penup()
        t.goto(t.position() + (size, 0))
        t.pendown()
        # Increase the size for the next square
        size += 20

    # Hide the turtle and display the window
    t.hideturtle()
    turtle.done()

draw_spiral_squares()