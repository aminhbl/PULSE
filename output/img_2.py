import turtle

def draw_spiral_squares():
    screen = turtle.Screen()
    screen.bgcolor("white")

    pen = turtle.Turtle()
    pen.speed(0)
    pen.penup()
    pen.goto(-200, -200)
    pen.pendown()

    size = 20
    for _ in range(6):
        for _ in range(4):
            pen.forward(size)
            pen.left(90)
        pen.penup()
        pen.forward(size)
        pen.right(90)
        pen.forward(size)
        pen.left(90)
        pen.pendown()
        size += 20

    pen.hideturtle()
    screen.mainloop()

draw_spiral_squares()