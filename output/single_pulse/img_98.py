import turtle

def draw_line(t, length):
    t.penup()
    t.forward(20)  # Leave a small space in the middle
    t.pendown()
    t.forward(length)
    t.penup()
    t.forward(10)  # Leave a small gap before the pentagon
    t.pendown()

def draw_pentagon(t, side_length):
    for _ in range(5):
        t.forward(side_length)
        t.right(72)

def draw_snowflake_arm(t, length, pentagon_side):
    draw_line(t, length)
    t.right(90)  # Orient the pentagon
    draw_pentagon(t, pentagon_side)
    t.left(90)  # Reorient back to original direction

def draw_snowflake(t, arm_length, pentagon_side):
    for _ in range(6):
        draw_snowflake_arm(t, arm_length, pentagon_side)
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.right(60)

# Setup turtle
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.color("black")
t.speed(0)  # Fastest drawing speed

# Draw the snowflake
draw_snowflake(t, 100, 30)

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()