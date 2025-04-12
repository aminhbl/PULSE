import turtle

def draw_snowflake_arm(t, length, gap, triangle_size):
    t.penup()
    t.forward(gap)
    t.pendown()
    t.forward(length)
    t.left(120)
    for _ in range(3):
        t.forward(triangle_size)
        t.left(120)
    t.right(120)
    t.penup()
    t.backward(length + gap)
    t.pendown()

def draw_snowflake(t, arm_length, gap, triangle_size):
    for _ in range(3):
        draw_snowflake_arm(t, arm_length, gap, triangle_size)
        t.right(120)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.speed(0)
    snowflake_turtle.color("blue")

    arm_length = 100
    gap = 20
    triangle_size = 20

    draw_snowflake(snowflake_turtle, arm_length, gap, triangle_size)

    snowflake_turtle.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()