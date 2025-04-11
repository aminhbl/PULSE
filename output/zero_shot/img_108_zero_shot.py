import turtle
import math

# Function to draw a circle and a square overlapping
def draw_cluster(t, size):
    # Draw circle
    t.penup()
    t.forward(size / 2)
    t.pendown()
    t.circle(size / 2)
    t.penup()
    t.backward(size / 2)
    t.pendown()
    
    # Draw square
    t.forward(size / 2)
    t.right(90)
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.penup()
    t.left(90)
    t.backward(size / 2)
    t.pendown()

# Setup turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)

# Parameters
size = 50  # Size of the circle's diameter and square's side
clusters = 3  # Number of clusters
angle = 360 / clusters  # Angle between clusters

# Draw clusters
for _ in range(clusters):
    draw_cluster(t, size)
    t.right(angle)

# Hide turtle and display window
t.hideturtle()
screen.mainloop()