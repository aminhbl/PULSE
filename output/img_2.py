import turtle

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.left(90)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.color("black")
    t.speed(0)

    # Starting size and position
    size = 20
    x, y = 0, 0

    # Draw 6 squares, each larger than the previous
    for i in range(6):
        t.penup()
        t.goto(x, y)
        t.pendown()
        draw_square(t, size)
        size += 20  # Increase size for the next square
        y -= 20    # Move the starting point down for the next square

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()