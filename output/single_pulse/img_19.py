import turtle

def draw_heptagon(t, size):
    t.pendown()
    for _ in range(7):
        t.forward(size)
        t.left(360 / 7)
    t.penup()

def draw_triangle(t, size):
    t.pendown()
    for _ in range(3):
        t.forward(size)
        t.left(120)
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

    # Calculate size based on canvas width
    size = 100

    # Draw heptagon
    t.goto(-size * 2, 0)
    draw_heptagon(t, size)

    # Draw triangle
    t.goto(size, 0)
    draw_triangle(t, size)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()