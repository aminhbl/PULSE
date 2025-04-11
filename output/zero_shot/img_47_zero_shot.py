import turtle

def draw_equilateral_triangle(t, side_length):
    for _ in range(3):
        t.forward(side_length)
        t.left(120)

def draw_six_triangles():
    screen = turtle.Screen()
    screen.setup(width=800, height=400)
    
    t = turtle.Turtle()
    t.pensize(3)
    t.color("black")
    
    side_length = 100
    for _ in range(6):
        draw_equilateral_triangle(t, side_length)
        t.penup()
        t.forward(side_length)
        t.pendown()
    
    screen.mainloop()

draw_six_triangles()