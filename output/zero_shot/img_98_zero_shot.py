import turtle

def draw_pentagon(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(72)

def draw_snowflake_arm(t, arm_length, pentagon_size):
    t.penup()
    t.forward(arm_length)
    t.pendown()
    t.forward(arm_length)
    t.penup()
    t.forward(arm_length)
    t.pendown()
    draw_pentagon(t, pentagon_size)
    t.penup()
    t.backward(3 * arm_length + pentagon_size)
    t.pendown()

def draw_snowflake(t, arm_length, pentagon_size):
    for _ in range(6):
        draw_snowflake_arm(t, arm_length, pentagon_size)
        t.right(60)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    snowflake = turtle.Turtle()
    snowflake.speed(0)
    snowflake.color("blue")

    arm_length = 20
    pentagon_size = 20

    draw_snowflake(snowflake, arm_length, pentagon_size)

    snowflake.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()