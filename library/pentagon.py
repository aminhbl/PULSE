import turtle

def draw_pentagon(side_length):
    # Set up the turtle
    turtle.bgcolor("white")
    turtle.color("black")
    turtle.pensize(2)
    turtle.speed(1)

    # Draw a pentagon
    for _ in range(5):
        turtle.forward(side_length)
        turtle.right(72)  # 360/5 = 72 degrees

    # Hide the turtle and finish
    turtle.hideturtle()
    turtle.done()

# Set the side length of the pentagon
side_length = 100

# Call the function to draw the pentagon
draw_pentagon(side_length)