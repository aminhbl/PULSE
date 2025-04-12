import turtle

def draw_pentagon(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(72)

def draw_snowflake_arm(t, length, gap, pentagon_size):
    t.penup()
    t.forward(gap)
    t.pendown()
    t.forward(length)
    t.penup()
    t.forward(gap)
    t.pendown()
    draw_pentagon(t, pentagon_size)
    t.penup()
    t.backward(length + 2 * gap + pentagon_size)
    t.pendown()

def draw_snowflake(t, arm_length, gap, pentagon_size):
    for _ in range(6):
        draw_snowflake_arm(t, arm_length, gap, pentagon_size)
        t.right(60)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    snowflake = turtle.Turtle()
    snowflake.color("blue")
    snowflake.speed(0)

    arm_length = 100
    gap = 20
    pentagon_size = 20

    draw_snowflake(snowflake, arm_length, gap, pentagon_size)

    snowflake.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()