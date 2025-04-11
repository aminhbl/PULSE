import turtle

def draw_snowflake_arm(t, length, circle_radius):
    t.penup()
    t.forward(length)
    t.pendown()
    t.forward(length)
    t.penup()
    t.forward(length)
    t.pendown()
    t.circle(circle_radius)
    t.penup()
    t.backward(3 * length + circle_radius * 2)
    t.pendown()

def draw_snowflake(t, arms, length, circle_radius):
    angle = 360 / arms
    for _ in range(arms):
        draw_snowflake_arm(t, length, circle_radius)
        t.right(angle)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.speed(0)  # Fastest speed

    arms = 8
    length = 20
    circle_radius = 5

    draw_snowflake(snowflake_turtle, arms, length, circle_radius)

    snowflake_turtle.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()