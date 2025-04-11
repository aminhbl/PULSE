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
    # Number of squares
    num_squares = 6
    # Increment size for each subsequent square
    increment = 20

    for i in range(num_squares):
        draw_square(t, size + i * increment)
        t.penup()
        t.goto(0, 0)
        t.pendown()

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()