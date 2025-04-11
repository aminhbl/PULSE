import turtle

def draw_triangle(t, length, angle):
    for _ in range(3):
        t.forward(length)
        t.left(120)

def main():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    # Calculate the center of the canvas
    center_x, center_y = 0, 0

    # Draw the first triangle (base at the bottom)
    t.goto(center_x, center_y)
    t.setheading(0)
    t.pendown()
    draw_triangle(t, 200, 0)
    t.penup()

    # Draw the second triangle (base pointing diagonally upward to the left)
    t.goto(center_x, center_y)
    t.setheading(120)
    t.pendown()
    draw_triangle(t, 200, 120)
    t.penup()

    # Draw the third triangle (base pointing diagonally upward to the right)
    t.goto(center_x, center_y)
    t.setheading(-120)
    t.pendown()
    draw_triangle(t, 200, -120)
    t.penup()

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()