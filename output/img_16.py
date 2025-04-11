import turtle

def draw_octagon(t, size):
    t.pendown()
    for _ in range(8):
        t.forward(size)
        t.left(45)
    t.penup()

def draw_semi_circle(t, radius):
    t.pendown()
    t.left(90)
    t.circle(radius, 180)
    t.penup()

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=400)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.pensize(3)
    t.color("black")
    t.penup()

    # Draw octagon on the left side
    t.goto(-200, 0)
    draw_octagon(t, 100)

    # Draw semi-circle on the right side
    t.goto(200, 50)
    draw_semi_circle(t, 100)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()