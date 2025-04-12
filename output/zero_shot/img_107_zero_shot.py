import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed

# Function to draw a circle
def draw_circle(radius):
    t.circle(radius)

# Function to draw a cluster of two touching circles
def draw_cluster(radius):
    draw_circle(radius)
    t.penup()
    t.forward(radius * 2)
    t.pendown()
    draw_circle(radius)
    t.penup()
    t.backward(radius * 2)
    t.pendown()

# Number of clusters
num_clusters = 5
# Radius of each circle
circle_radius = 20
# Distance from the center to the center of each cluster
cluster_distance = circle_radius * 4

# Draw clusters in a circular pattern
for i in range(num_clusters):
    angle = (360 / num_clusters) * i
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(cluster_distance)
    t.pendown()
    draw_cluster(circle_radius)

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()