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
    t.speed(1)

    size = 100  # Size of the squares

    # Draw the first square
    draw_square(t, size)

    # Move to the common vertex for the second square
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.left(90)

    # Draw the second square
    draw_square(t, size)

    # Move to the common vertex for the third square
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.left(90)

    # Draw the third square
    draw_square(t, size)

    # Hide the turtle and display the window
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()