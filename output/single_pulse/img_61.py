import turtle
import math

def draw_square(t, center, size):
    t.penup()
    t.goto(center[0] - size / 2, center[1] - size / 2)
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.left(90)

def draw_rotated_square(t, center, size):
    t.penup()
    t.goto(center[0], center[1])
    t.setheading(45)
    t.forward(size / math.sqrt(2))
    t.setheading(135)
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.left(90)

def draw_diagonal_lines(t, center, size):
    # Diagonals for upright square
    t.penup()
    t.goto(center[0] - size / 2, center[1])
    t.pendown()
    t.goto(center[0] + size / 2, center[1])
    
    t.penup()
    t.goto(center[0], center[1] - size / 2)
    t.pendown()
    t.goto(center[0], center[1] + size / 2)
    
    # Diagonals for rotated square
    offset = size / math.sqrt(2)
    t.penup()
    t.goto(center[0] - offset, center[1] - offset)
    t.pendown()
    t.goto(center[0] + offset, center[1] + offset)
    
    t.penup()
    t.goto(center[0] - offset, center[1] + offset)
    t.pendown()
    t.goto(center[0] + offset, center[1] - offset)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.color("black")
    
    center = (0, 0)
    size = 200
    
    draw_square(t, center, size)
    draw_rotated_square(t, center, size)
    draw_diagonal_lines(t, center, size)
    
    t.hideturtle()
    screen.mainloop()

main()