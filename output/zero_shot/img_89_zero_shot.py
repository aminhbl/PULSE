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

def draw_snowflake(t, num_arms, arm_length, pentagon_size):
    angle = 360 / num_arms
    for _ in range(num_arms):
        draw_snowflake_arm(t, arm_length, pentagon_size)
        t.right(angle)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.speed(0)
    snowflake_turtle.color("blue")

    num_arms = 3
    arm_length = 20
    pentagon_size = 30

    draw_snowflake(snowflake_turtle, num_arms, arm_length, pentagon_size)

    snowflake_turtle.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()