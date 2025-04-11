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
    t.speed(0)  # Fastest drawing speed

    sizes = [20, 40, 60, 80, 100]  # Sizes of the squares

    for size in sizes:
        draw_square(t, size)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()