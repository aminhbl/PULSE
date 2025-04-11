import turtle

def draw_line(t, length):
    t.forward(length)

def draw_triangle(t, side_length):
    for _ in range(3):
        t.forward(side_length)
        t.left(120)

def draw_pattern():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.color("black")
    t.speed(0)  # Fastest speed

    central_point = (0, 0)
    line_length = 100
    triangle_side_length = 50

    for angle in range(0, 360, 45):
        t.penup()
        t.goto(central_point)
        t.setheading(angle)
        t.pendown()
        
        # Draw the line
        draw_line(t, line_length)
        
        # Draw the triangle
        t.penup()
        t.forward(triangle_side_length / 2)
        t.pendown()
        draw_triangle(t, triangle_side_length)
        t.penup()
        t.backward(triangle_side_length / 2)
        t.pendown()

    t.hideturtle()
    screen.mainloop()

draw_pattern()