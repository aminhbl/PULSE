import turtle
import math

def draw_curve(t, length, angle, extent):
    for _ in range(extent):
        t.forward(length)
        t.left(angle)

def draw_flower():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.width(2)

    num_petals = 6
    angle_between_petals = 360 / num_petals
    curve_length = 2
    curve_angle = 1
    curve_extent = 60

    for _ in range(num_petals):
        t.penup()
        t.goto(0, 0)
        t.pendown()
        draw_curve(t, curve_length, curve_angle, curve_extent)
        t.left(angle_between_petals)

    t.hideturtle()
    screen.mainloop()

draw_flower()