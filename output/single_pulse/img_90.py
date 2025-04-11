import turtle

def draw_line(t, length):
    t.penup()
    t.forward(length)
    t.pendown()
    t.forward(20)  # Draw the line with a gap at the start
    t.penup()
    t.forward(20)  # Move to the position for the triangle
    t.pendown()

def draw_triangle(t, size, orientation):
    if orientation == 'up':
        for _ in range(3):
            t.forward(size)
            t.left(120)
    elif orientation == 'down':
        for _ in range(3):
            t.forward(size)
            t.right(120)

def draw_snowflake_arm(t, length, triangle_size, orientation):
    draw_line(t, length)
    draw_triangle(t, triangle_size, orientation)

def draw_snowflake():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.color("black")
    t.speed(0)
    
    num_arms = 6
    arm_length = 50
    triangle_size = 20
    
    for i in range(num_arms):
        draw_snowflake_arm(t, arm_length, triangle_size, 'up' if i % 2 == 0 else 'down')
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.right(360 / num_arms)
    
    t.hideturtle()
    screen.mainloop()

draw_snowflake()