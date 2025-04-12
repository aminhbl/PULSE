import turtle
import math

# Function to draw a circle
def draw_circle(t, radius):
    t.circle(radius)

# Function to draw a cluster of two touching circles
def draw_cluster(t, radius):
    draw_circle(t, radius)
    t.penup()
    t.forward(2 * radius)
    t.pendown()
    draw_circle(t, radius)
    t.penup()
    t.backward(2 * radius)
    t.pendown()

# Setup the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")
t.color("black")

# Parameters
radius = 50
num_clusters = 5
angle_between_clusters = 360 / num_clusters
distance_from_center = 3 * radius  # Distance from the center to each cluster

# Draw the clusters in a circular pattern
for i in range(num_clusters):
    t.penup()
    # Calculate the position for each cluster
    angle = math.radians(i * angle_between_clusters)
    x = distance_from_center * math.cos(angle)
    y = distance_from_center * math.sin(angle)
    t.goto(x, y)
    t.setheading(t.towards(0, 0) + 90)  # Point the turtle towards the center
    t.pendown()
    draw_cluster(t, radius)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()