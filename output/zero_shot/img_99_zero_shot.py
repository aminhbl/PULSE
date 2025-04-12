import turtle
import math

# Function to draw a pentagon
def draw_pentagon(t, size, angle):
    for _ in range(5):
        t.forward(size)
        t.right(72 + angle)

# Function to draw a cluster of two overlapping pentagons
def draw_cluster(t, size, overlap_angle):
    draw_pentagon(t, size, 0)
    t.penup()
    t.forward(size / 5)  # Move slightly forward for overlap
    t.pendown()
    draw_pentagon(t, size, overlap_angle)
    t.penup()
    t.backward(size / 5)  # Move back to original position
    t.pendown()

# Setup turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# Parameters
num_clusters = 5
size = 100
angle_increment = 10
overlap_angle = 0

# Draw clusters in a circular arrangement
for i in range(num_clusters):
    t.penup()
    t.goto(0, 0)
    t.setheading(90)  # Start facing upwards
    t.right(i * (360 / num_clusters))  # Rotate to the cluster position
    t.forward(150)  # Move to the cluster position
    t.pendown()
    
    draw_cluster(t, size, overlap_angle)
    
    overlap_angle += angle_increment  # Gradually change the overlap angle

# Hide turtle and display the window
t.hideturtle()
screen.mainloop()