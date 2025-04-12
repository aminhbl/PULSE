import turtle

def draw_snowflake_arm(t, length, gap, square_size):
    t.penup()
    t.forward(gap)
    t.pendown()
    t.forward(length)
    t.penup()
    t.forward(square_size / 2)
    t.pendown()
    for _ in range(4):
        t.forward(square_size)
        t.right(90)
    t.penup()
    t.backward(length + gap + square_size / 2)
    t.pendown()

def draw_snowflake(t, arms, length, gap, square_size):
    angle = 360 / arms
    for _ in range(arms):
        draw_snowflake_arm(t, length, gap, square_size)
        t.right(angle)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    snowflake = turtle.Turtle()
    snowflake.speed(0)
    snowflake.color("blue")

    arms = 6
    length = 100
    gap = 20
    square_size = 20

    draw_snowflake(snowflake, arms, length, gap, square_size)

    snowflake.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()