import turtle

def draw_pentagon(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(72)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.color("black")
    t.speed(0)

    size = 100  # Length of each side of the pentagon
    for _ in range(5):
        draw_pentagon(t, size)
        t.penup()
        t.forward(size)
        t.pendown()

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()