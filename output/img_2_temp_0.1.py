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

    # Starting size of the smallest square
    size = 20

    # Draw 6 squares, each larger than the previous
    for i in range(6):
        draw_square(t, size)
        size += 20  # Increase the size for the next square

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()