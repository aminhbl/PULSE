import turtle

def draw_line(t, length):
    t.penup()
    t.forward(length)
    t.pendown()
    t.backward(length)

def draw_square(t, size):
    t.penup()
    t.forward(size / 2)
    t.right(90)
    t.forward(size / 2)
    t.left(90)
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.penup()
    t.left(90)
    t.forward(size / 2)
    t.right(90)
    t.backward(size / 2)

def draw_snowflake():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.color("black")
    t.speed(0)
    
    num_arms = 6
    angle = 360 / num_arms
    line_length = 100
    square_size = 20
    gap = 10
    
    for _ in range(num_arms):
        t.penup()
        t.goto(0, 0)
        t.setheading(angle * _)
        t.forward(gap)
        draw_line(t, line_length - gap)
        t.forward(line_length - gap)
        draw_square(t, square_size)
    
    t.hideturtle()
    screen.mainloop()

draw_snowflake()