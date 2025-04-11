import turtle

def draw_semi_circle(t, radius):
    t.begin_fill()
    t.circle(radius, 180)
    t.end_fill()

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.color("black")
    t.pensize(3)
    t.speed(0)

    radius = 50
    spacing = 20
    total_width = 6 * (radius + spacing) - spacing

    # Move turtle to starting position
    t.penup()
    t.goto(-total_width / 2, 0)
    t.pendown()

    for _ in range(6):
        draw_semi_circle(t, radius)
        t.penup()
        t.forward(radius + spacing)
        t.pendown()

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()