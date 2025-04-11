import turtle

def draw_octagon(t, size):
    for _ in range(8):
        t.forward(size)
        t.left(45)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.color("black")
    t.pensize(2)
    t.speed(0)

    # Size of the octagon
    octagon_size = 50

    # Draw the first octagon
    t.penup()
    t.goto(-octagon_size * 2, 0)
    t.pendown()
    draw_octagon(t, octagon_size)

    # Draw the second octagon
    t.penup()
    t.goto(octagon_size * 2, 0)
    t.pendown()
    draw_octagon(t, octagon_size)

    # Draw the connecting line
    t.penup()
    t.goto(-octagon_size, -octagon_size / 2)
    t.pendown()
    t.forward(octagon_size * 2)

    # Hide the turtle
    t.hideturtle()

    # Keep the window open
    screen.mainloop()

if __name__ == "__main__":
    main()