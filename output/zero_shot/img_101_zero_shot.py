import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
pen = turtle.Turtle()
pen.speed(0)  # Fastest speed
pen.hideturtle()

# Function to draw a pentagon
def draw_pentagon(size):
    for _ in range(5):
        pen.forward(size)
        pen.right(72)

# Function to draw a circle
def draw_circle(radius):
    pen.circle(radius)

# Function to draw a cluster (a pentagon overlapping with a circle)
def draw_cluster(size, radius):
    draw_pentagon(size)
    pen.penup()
    pen.goto(pen.xcor() + size / 2, pen.ycor() - radius)
    pen.pendown()
    draw_circle(radius)
    pen.penup()
    pen.goto(pen.xcor() - size / 2, pen.ycor() + radius)
    pen.pendown()

# Parameters
num_clusters = 8
cluster_distance = 100
pentagon_size = 50
circle_radius = 30

# Draw clusters in a circular arrangement
for i in range(num_clusters):
    angle = i * (360 / num_clusters)
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(angle)
    pen.forward(cluster_distance)
    pen.pendown()
    draw_cluster(pentagon_size, circle_radius)

# Hide the turtle and display the window
pen.hideturtle()
screen.mainloop()