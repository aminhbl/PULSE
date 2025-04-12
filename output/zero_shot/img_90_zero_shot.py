import turtle

def draw_snowflake_arm(t, length, gap, triangle_size, orientation):
    t.penup()
    t.forward(gap)
    t.pendown()
    t.forward(length)
    t.penup()
    t.forward(triangle_size)
    t.pendown()
    
    if orientation == "up":
        t.left(120)
    else:
        t.right(120)
    
    for _ in range(3):
        t.forward(triangle_size)
        if orientation == "up":
            t.left(120)
        else:
            t.right(120)
    
    if orientation == "up":
        t.right(120)
    else:
        t.left(120)
    
    t.penup()
    t.backward(length + gap + triangle_size)
    t.pendown()

def draw_snowflake():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.color("blue")
    
    num_arms = 6
    arm_length = 100
    gap = 20
    triangle_size = 20
    
    for i in range(num_arms):
        orientation = "up" if i % 2 == 0 else "down"
        draw_snowflake_arm(t, arm_length, gap, triangle_size, orientation)
        t.right(360 / num_arms)
    
    t.hideturtle()
    screen.mainloop()

draw_snowflake()