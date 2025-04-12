import turtle
import math

# Function to draw a pentagon
def draw_pentagon(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(72)

# Function to draw a cluster of two overlapping pentagons
def draw_cluster(t, size, angle_offset, overlap_offset):
    # Draw the first pentagon
    draw_pentagon(t, size)
    
    # Move to the starting position for the second pentagon
    t.penup()
    t.forward(overlap_offset)
    t.right(angle_offset)
    t.pendown()
    
    # Draw the second pentagon
    draw_pentagon(t, size)
    
    # Reset position
    t.penup()
    t.left(angle_offset)
    t.backward(overlap_offset)
    t.pendown()

# Setup the turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.color("black")

# Define parameters
circle_radius = 200
pentagon_size = 50
angle_increment = 5
overlap_increment = 10

# Draw clusters in a circular arrangement
for i in range(5):
    # Calculate the angle for the current cluster
    angle = i * 72
    
    # Move to the starting position for the cluster
    t.penup()
    t.goto(0, 0)
    t.setheading(90 - angle)
    t.forward(circle_radius)
    t.pendown()
    
    # Draw the cluster
    draw_cluster(t, pentagon_size, angle_increment * i, overlap_increment * i)

# Hide the turtle and display the result
t.hideturtle()
screen.mainloop()