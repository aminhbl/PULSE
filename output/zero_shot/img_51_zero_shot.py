import turtle
import math

def draw_octagon(t, size):
    for _ in range(8):
        t.forward(size)
        t.left(45)

def draw_flower_of_octagons():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    
    num_octagons = 6
    angle_between = 360 / num_octagons
    radius = 100
    octagon_size = 100
    
    for i in range(num_octagons):
        t.goto(0, 0)
        t.setheading(angle_between * i)
        t.forward(radius)
        t.pendown()
        draw_octagon(t, octagon_size)
        t.penup()
    
    t.hideturtle()
    screen.mainloop()

draw_flower_of_octagons()