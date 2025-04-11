import turtle

def draw_semicircle(t, radius):
    t.circle(radius, 180)

def draw_pinwheel():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, 0)
    t.pendown()

    radius = 100  # Radius of the semicircles

    for _ in range(3):
        draw_semicircle(t, radius)
        t.left(120)

    t.hideturtle()
    screen.mainloop()

draw_pinwheel()