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

def draw_snowflake(t, arms, length, gap, triangle_size):
    angle = 360 / arms
    for _ in range(arms):
        draw_snowflake_arm(t, length, gap, triangle_size)
        t.right(angle)

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")

snowflake_turtle = turtle.Turtle()
snowflake_turtle.speed(0)  # Fastest speed

# Parameters for the snowflake
arms = 8
line_length = 100
gap = 20
triangle_size = 20

# Draw the snowflake
draw_snowflake(snowflake_turtle, arms, line_length, gap, triangle_size)

# Hide the turtle and display the window
snowflake_turtle.hideturtle()
screen.mainloop()