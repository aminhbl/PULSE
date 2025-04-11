import turtle

def draw_nonagon(t, side_length):
    t.pendown()
    t.pensize(3)
    t.pencolor("black")
    for _ in range(9):
        t.forward(side_length)
        t.left(40)
    t.penup()

def draw_semi_circle(t, radius):
    t.pendown()
    t.pensize(3)
    t.pencolor("black")
    t.circle(radius, 180)
    t.penup()

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    # Draw nonagon on the left side
    t.goto(-200, 0)
    draw_nonagon(t, 100)

    # Draw semi-circle on the right side, slightly above the nonagon
    t.goto(100, 100)
    t.setheading(-45)  # Rotate 45 degrees to the right
    draw_semi_circle(t, 50)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()