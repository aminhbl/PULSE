import turtle

def draw_pentagon(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(72)

def draw_snowflake_arm(t, line_length, gap, pentagon_size):
    t.penup()
    t.forward(gap)
    t.pendown()
    t.forward(line_length)
    t.penup()
    t.forward(gap)
    t.pendown()
    draw_pentagon(t, pentagon_size)

def draw_snowflake(t, arms, line_length, gap, pentagon_size):
    angle = 360 / arms
    for _ in range(arms):
        draw_snowflake_arm(t, line_length, gap, pentagon_size)
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.right(angle)

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")

snowflake_turtle = turtle.Turtle()
snowflake_turtle.color("blue")
snowflake_turtle.speed(0)

# Draw the snowflake
draw_snowflake(snowflake_turtle, 3, 100, 20, 30)

# Hide the turtle and display the window
snowflake_turtle.hideturtle()
screen.mainloop()