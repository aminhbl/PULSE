import turtle
import math

def draw_curve(t, length, angle):
    for _ in range(60):
        t.forward(length)
        t.left(angle)

def draw_flower():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  # Fastest speed

    num_lines = 6
    angle_between_lines = 360 / num_lines
    curve_length = 2
    curve_angle = 3

    for _ in range(num_lines):
        t.penup()
        t.goto(0, 0)
        t.pendown()
        draw_curve(t, curve_length, curve_angle)
        t.left(angle_between_lines)

    t.hideturtle()
    screen.mainloop()

draw_flower()