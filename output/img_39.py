import turtle

def draw_triangle(t, side_length):
    t.begin_fill()
    for _ in range(3):
        t.forward(side_length)
        t.left(120)
    t.end_fill()

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.color("black")
    t.pensize(3)
    t.speed(0)

    # Set the starting position
    t.penup()
    t.goto(-200, 0)
    t.pendown()

    # Draw the base line
    base_length = 400
    t.forward(base_length)

    # Draw four triangles
    side_length = base_length / 4
    for _ in range(4):
        t.penup()
        t.goto(t.xcor() - side_length, 0)
        t.pendown()
        draw_triangle(t, side_length)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()