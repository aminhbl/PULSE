import turtle

def draw_line(t, start, end):
    t.penup()
    t.goto(start)
    t.pendown()
    t.goto(end)

def draw_square(t, center, size):
    t.penup()
    t.goto(center[0] - size / 2, center[1] - size / 2)
    t.setheading(0)
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.left(90)

def main():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.title("Y-shaped Structure with Squares")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    # Define the Y-shaped structure
    center = (0, 0)
    line_length = 100
    square_size = 30

    # Draw the vertical line
    vertical_end = (center[0], center[1] + line_length)
    draw_line(t, center, vertical_end)

    # Draw the diagonal lines
    angle = 45
    left_diagonal_end = (vertical_end[0] - line_length * 0.7, vertical_end[1] + line_length * 0.7)
    right_diagonal_end = (vertical_end[0] + line_length * 0.7, vertical_end[1] + line_length * 0.7)

    draw_line(t, vertical_end, left_diagonal_end)
    draw_line(t, vertical_end, right_diagonal_end)

    # Draw squares at the end of each line
    draw_square(t, vertical_end, square_size)
    draw_square(t, left_diagonal_end, square_size)
    draw_square(t, right_diagonal_end, square_size)

    screen.mainloop()

if __name__ == "__main__":
    main()