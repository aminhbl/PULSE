import turtle

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.left(90)

def draw_spiral_squares():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.color("black")
    t.speed(0)
    
    size = 20  # Starting size of the smallest square
    increment = 20  # Increment size for each subsequent square
    
    for _ in range(8):
        draw_square(t, size)
        size += increment
        t.penup()
        t.goto(-increment/2, -increment/2)
        t.pendown()
    
    t.hideturtle()
    screen.mainloop()

draw_spiral_squares()