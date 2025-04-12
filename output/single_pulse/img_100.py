import turtle

def draw_line(t, length):
    t.penup()
    t.forward(length)
    t.pendown()
    t.forward(length)
    t.penup()
    t.backward(2 * length)
    t.pendown()

def draw_semi_circle(t, radius):
    t.penup()
    t.forward(radius)
    t.pendown()
    t.circle(radius, 180)
    t.penup()
    t.backward(radius)
    t.pendown()

def draw_snowflake_arm(t, line_length, gap, semi_circle_radius):
    draw_line(t, line_length)
    t.penup()
    t.forward(gap)
    t.pendown()
    draw_semi_circle(t, semi_circle_radius)

def draw_snowflake(t, arms, line_length, gap, semi_circle_radius):
    angle = 360 / arms
    for _ in range(arms):
        draw_snowflake_arm(t, line_length, gap, semi_circle_radius)
        t.right(angle)

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.color("black")
t.speed(0)  # Fastest speed

# Parameters
arms = 8
line_length = 50
gap = 10
semi_circle_radius = 20

# Draw the snowflake
t.penup()
t.goto(0, 0)
t.pendown()
draw_snowflake(t, arms, line_length, gap, semi_circle_radius)

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()