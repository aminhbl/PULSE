import turtle

def draw_triangle(t, size):
    for _ in range(3):
        t.forward(size)
        t.left(120)

def draw_arm(t, size, space):
    t.penup()
    t.forward(space)
    t.pendown()
    t.forward(size)
    t.penup()
    t.forward(space)
    t.pendown()
    draw_triangle(t, size)

def draw_snowflake(t, arms, size, space):
    for _ in range(arms):
        draw_arm(t, size, space)
        t.left(360 / arms)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    snowflake = turtle.Turtle()
    snowflake.color("blue")
    snowflake.speed(0)

    arms = 3
    size = 20
    space = 10

    draw_snowflake(snowflake, arms, size, space)

    snowflake.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()