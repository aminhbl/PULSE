import turtle

def draw_snowflake_arm(t, length, gap, circle_radius):
    t.penup()
    t.forward(gap)
    t.pendown()
    t.forward(length)
    t.penup()
    t.forward(circle_radius)
    t.pendown()
    t.circle(circle_radius)
    t.penup()
    t.backward(length + gap + circle_radius)
    t.pendown()

def draw_snowflake(t, arms, length, gap, circle_radius):
    angle = 360 / arms
    for _ in range(arms):
        draw_snowflake_arm(t, length, gap, circle_radius)
        t.right(angle)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    snowflake = turtle.Turtle()
    snowflake.speed(0)  # Fastest speed

    arms = 8
    arm_length = 100
    gap = 20
    circle_radius = 15

    draw_snowflake(snowflake, arms, arm_length, gap, circle_radius)

    snowflake.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()