import turtle

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_snowflake_arm(t, arm_length, square_size):
    t.penup()
    t.forward(arm_length)
    t.pendown()
    t.forward(arm_length)
    t.penup()
    t.forward(arm_length)
    t.pendown()
    draw_square(t, square_size)
    t.penup()
    t.backward(3 * arm_length + square_size)
    t.pendown()

def draw_snowflake(t, num_arms, arm_length, square_size):
    angle = 360 / num_arms
    for i in range(num_arms):
        draw_snowflake_arm(t, arm_length, square_size)
        t.right(angle)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    snowflake = turtle.Turtle()
    snowflake.speed(0)
    snowflake.color("blue")

    num_arms = 6
    arm_length = 20
    square_size = 10

    draw_snowflake(snowflake, num_arms, arm_length, square_size)

    snowflake.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()