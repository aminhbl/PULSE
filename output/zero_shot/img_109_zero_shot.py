import turtle
import math

def draw_pentagon(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(72)

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_cluster(t, size, angle_offset):
    # Draw pentagon
    draw_pentagon(t, size)
    
    # Position for square
    t.penup()
    t.forward(size / 2)
    t.right(90)
    t.forward(size / 2)
    t.left(90 + angle_offset)
    t.pendown()
    
    # Draw square
    draw_square(t, size)
    
    # Reset position
    t.penup()
    t.left(90 + angle_offset)
    t.backward(size / 2)
    t.left(90)
    t.backward(size / 2)
    t.right(90)
    t.pendown()

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    
    size = 50
    angle_between_clusters = 72
    
    for i in range(5):
        draw_cluster(t, size, i * 15)
        t.penup()
        t.right(angle_between_clusters)
        t.forward(size * 3)
        t.pendown()
    
    t.hideturtle()
    screen.mainloop()

main()