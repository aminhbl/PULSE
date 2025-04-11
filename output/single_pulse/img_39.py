import turtle

def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)

def draw_bold_triangle(side_length):
    turtle.pensize(3)  # Set the pen size to bold
    turtle.pendown()
    draw_triangle(side_length)
    turtle.penup()

def main():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200, 0)  # Start position for the first triangle

    side_length = 100  # Length of each side of the triangle

    for _ in range(4):
        draw_bold_triangle(side_length)
        turtle.forward(side_length)  # Move to the start position for the next triangle

    turtle.hideturtle()
    turtle.done()

main()