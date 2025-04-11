import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Function to draw a pentagon
def draw_pentagon(t, size, angle):
    for _ in range(5):
        t.forward(size)
        t.right(72 + angle)

# Function to draw a cluster of two overlapping pentagons
def draw_cluster(t, size, overlap_angle, overlap_distance):
    # Draw the first pentagon
    draw_pentagon(t, size, 0)
    # Move to the starting position of the second pentagon
    t.penup()
    t.forward(overlap_distance)
    t.pendown()
    # Draw the second pentagon with a slight rotation
    draw_pentagon(t, size, overlap_angle)

# Parameters
num_clusters = 5
cluster_radius = 150
pentagon_size = 50
overlap_angles = [5, 10, 15, 20, 25]  # Varying overlap angles
overlap_distances = [10, 15, 20, 25, 30]  # Varying overlap distances

# Draw clusters in a circular pattern
for i in range(num_clusters):
    # Calculate the angle for the current cluster
    angle = i * (360 / num_clusters)
    # Move to the starting position for the current cluster
    pen.penup()
    pen.goto(cluster_radius * math.cos(math.radians(angle)), cluster_radius * math.sin(math.radians(angle)))
    pen.pendown()
    pen.setheading(angle)
    # Draw the cluster
    draw_cluster(pen, pentagon_size, overlap_angles[i], overlap_distances[i])

# Hide the turtle and display the window
pen.hideturtle()
turtle.done()