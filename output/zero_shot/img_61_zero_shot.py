import turtle
import math

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.left(90)

def draw_diagonals(t, size):
    half_size = size / 2
    t.penup()
    t.goto(-half_size, 0)
    t.pendown()
    t.goto(half_size, 0)
    t.penup()
    t.goto(0, -half_size)
    t.pendown()
    t.goto(0, half_size)

def draw_rotated_square(t, size):
    angle = 45
    t.left(angle)
    draw_square(t, size * math.sqrt(2))
    t.right(angle)

def draw_star():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.title("Eight-Pointed Star")

    star_turtle = turtle.Turtle()
    star_turtle.speed(0)

    size = 200

    # Draw upright square
    draw_square(star_turtle, size)
    draw_diagonals(star_turtle, size)

    # Draw rotated square
    draw_rotated_square(star_turtle, size)
    draw_diagonals(star_turtle, size * math.sqrt(2))

    star_turtle.hideturtle()
    screen.mainloop()

draw_star()