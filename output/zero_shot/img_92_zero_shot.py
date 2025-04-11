import turtle

def draw_triangle(t, size):
    for _ in range(3):
        t.forward(size)
        t.left(120)

def draw_snowflake_arm(t, arm_length, triangle_size):
    t.penup()
    t.forward(arm_length)
    t.pendown()
    t.forward(arm_length)
    t.penup()
    t.forward(arm_length)
    t.pendown()
    draw_triangle(t, triangle_size)
    t.penup()
    t.backward(3 * arm_length + triangle_size)
    t.pendown()

def draw_snowflake(t, num_arms, arm_length, triangle_size):
    angle = 360 / num_arms
    for _ in range(num_arms):
        draw_snowflake_arm(t, arm_length, triangle_size)
        t.left(angle)

def main():
    screen = turtle.Screen()
    screen.bgcolor("lightblue")

    snowflake = turtle.Turtle()
    snowflake.speed(0)
    snowflake.color("blue")

    num_arms = 8
    arm_length = 20
    triangle_size = 15

    draw_snowflake(snowflake, num_arms, arm_length, triangle_size)

    snowflake.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()