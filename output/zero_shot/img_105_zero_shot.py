import turtle
import math

# Function to draw a semicircle
def draw_semicircle(t, radius, direction):
    t.circle(radius, 180 if direction == 'left' else -180)

# Function to draw a cluster of semicircles
def draw_cluster(t, large_radius, small_radius, angle):
    # Position the turtle for the large semicircle
    t.penup()
    t.setheading(angle)
    t.forward(large_radius)
    t.pendown()
    t.setheading(angle + 90)
    draw_semicircle(t, large_radius, 'left')
    
    # Position the turtle for the small semicircle
    t.penup()
    t.setheading(angle)
    t.forward(large_radius + small_radius)
    t.pendown()
    t.setheading(angle - 90)
    draw_semicircle(t, small_radius, 'right')

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)

# Parameters
large_radius = 100
small_radius = 50
num_clusters = 3
angle_between_clusters = 360 / num_clusters
distance_from_center = large_radius + small_radius

# Draw the clusters
for i in range(num_clusters):
    angle = i * angle_between_clusters
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(distance_from_center)
    t.pendown()
    draw_cluster(t, large_radius, small_radius, angle)

# Hide the turtle and display the result
t.hideturtle()
screen.mainloop()