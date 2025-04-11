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

    size_increment = 20
    initial_size = 20

    for i in range(7):
        draw_square(t, initial_size + i * size_increment)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()