import turtle

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_snowflake_arm(t, arm_length, square_size, angle):
    t.penup()
    t.forward(arm_length)
    t.pendown()
    t.forward(arm_length)
    t.penup()
    t.forward(arm_length)
    t.pendown()
    draw_square(t, square_size)
    t.penup()
    t.backward(3 * arm_length + square_size / 2)
    t.right(angle)

def draw_snowflake(t, num_arms, arm_length, square_size):
    angle = 360 / num_arms
    for _ in range(num_arms):
        draw_snowflake_arm(t, arm_length, square_size, angle)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    snowflake = turtle.Turtle()
    snowflake.speed(0)
    snowflake.color("blue")

    num_arms = 7
    arm_length = 20
    square_size = 20

    draw_snowflake(snowflake, num_arms, arm_length, square_size)

    snowflake.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()