import turtle

def draw_semi_circle(t, radius):
    t.begin_fill()
    t.circle(radius, 180)  # Draw a semi-circle
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

    for _ in range(6):
        draw_semi_circle(t, radius)
        t.penup()
        t.forward(radius * 2 + spacing)
        t.pendown()

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()