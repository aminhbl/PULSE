import turtle

def draw_hexagon(t, size):
    for _ in range(6):
        t.forward(size)
        t.left(60)

def draw_honeycomb():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    
    # Draw the first hexagon
    t.goto(-50, 0)
    t.pendown()
    draw_hexagon(t, 100)
    t.penup()
    
    # Draw the second hexagon (top right)
    t.goto(0, 86.6)  # 86.6 is the height of the hexagon (size * sqrt(3)/2)
    t.pendown()
    draw_hexagon(t, 100)
    t.penup()
    
    # Draw the third hexagon (bottom right)
    t.goto(50, 0)
    t.pendown()
    draw_hexagon(t, 100)
    t.penup()
    
    t.hideturtle()
    screen.mainloop()

draw_honeycomb()