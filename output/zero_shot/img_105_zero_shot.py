import turtle
import math

# Function to draw an arc
def draw_arc(t, radius, extent):
    t.circle(radius, extent)

# Function to draw a cluster of arcs
def draw_cluster(t, large_radius, small_radius, extent):
    draw_arc(t, large_radius, extent)
    t.penup()
    t.setheading(t.heading() + 180)
    t.forward(large_radius - small_radius)
    t.setheading(t.heading() + 180)
    t.pendown()
    draw_arc(t, small_radius, -extent)
    t.penup()
    t.setheading(t.heading() + 180)
    t.forward(large_radius - small_radius)
    t.setheading(t.heading() + 180)
    t.pendown()

# Setup the turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.width(2)

# Parameters
large_radius = 100
small_radius = 50
extent = 90
num_clusters = 3
angle_between_clusters = 360 / num_clusters

# Draw clusters in a circular pattern
for i in range(num_clusters):
    t.penup()
    t.goto(0, 0)
    t.setheading(angle_between_clusters * i)
    t.forward(large_radius + small_radius)
    t.setheading(t.heading() + 90)
    t.pendown()
    draw_cluster(t, large_radius, small_radius, extent)

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()