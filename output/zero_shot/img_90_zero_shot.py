import turtle

def draw_triangle(t, size, orientation):
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        if orientation == "up":
            t.left(120)
        else:
            t.right(120)
    t.end_fill()

def draw_snowflake_arm(t, length, triangle_size, orientation):
    t.penup()
    t.forward(length)
    t.pendown()
    t.forward(length)
    draw_triangle(t, triangle_size, orientation)
    t.penup()
    t.backward(2 * length)
    t.pendown()

def draw_snowflake(t, arms, length, triangle_size):
    for i in range(arms):
        orientation = "up" if i % 2 == 0 else "down"
        draw_snowflake_arm(t, length, triangle_size, orientation)
        t.right(360 / arms)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.color("blue")

    arms = 6
    length = 20
    triangle_size = 10

    draw_snowflake(t, arms, length, triangle_size)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()