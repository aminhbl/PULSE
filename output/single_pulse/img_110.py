import turtle
import math

# Function to draw a pentagon
def draw_pentagon(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(72)

# Function to draw a square
def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Function to draw a cluster of a pentagon and a square
def draw_cluster(t, size, square_angle):
    # Draw pentagon
    draw_pentagon(t, size)
    
    # Position for square
    t.penup()
    t.forward(size / 2)
    t.right(90)
    t.forward(size / 2)
    t.left(90 + square_angle)
    t.pendown()
    
    # Draw square
    draw_square(t, size)
    
    # Reset position
    t.penup()
    t.left(90 + square_angle)
    t.backward(size / 2)
    t.left(90)
    t.backward(size / 2)
    t.pendown()

# Setup turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.color("black")

# Size of the shapes
size = 100

# Angles for square orientation in each cluster
square_angles = [0, 15, 30, 45, 60, 75]

# Draw six clusters in a circular pattern
for i in range(6):
    # Draw cluster
    draw_cluster(t, size, square_angles[i])
    
    # Move to next cluster position
    t.penup()
    t.forward(size * 2)
    t.right(60)
    t.pendown()

# Hide turtle and display window
t.hideturtle()
screen.mainloop()