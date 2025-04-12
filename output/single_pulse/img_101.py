import turtle
import math

# Function to draw a circle
def draw_circle(t, radius):
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.circle(radius)
    t.penup()
    t.goto(0, 0)
    t.pendown()

# Function to draw a pentagon
def draw_pentagon(t, size):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    for _ in range(5):
        t.forward(size)
        t.right(72)
    t.penup()
    t.goto(0, 0)
    t.pendown()

# Function to draw a cluster (circle + pentagon)
def draw_cluster(t, radius, size):
    draw_circle(t, radius)
    draw_pentagon(t, size)

# Setup turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.color("black")

# Central point and radius for the circular arrangement
central_radius = 150
cluster_radius = 50
pentagon_size = 100

# Calculate the angle between each cluster
angle_between_clusters = 360 / 8

# Draw the clusters
for i in range(8):
    angle = math.radians(i * angle_between_clusters)
    x = central_radius * math.cos(angle)
    y = central_radius * math.sin(angle)
    
    # Move turtle to the position for the cluster
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # Draw the cluster
    draw_cluster(t, cluster_radius, pentagon_size)

# Hide the turtle and display the result
t.hideturtle()
screen.mainloop()