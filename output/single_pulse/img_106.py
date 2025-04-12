import turtle
import math

# Function to draw a circle
def draw_circle(t, radius):
    t.circle(radius)

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.penup()

# Constants
central_circle_radius = 20
large_circle_radius = 50
small_circle_radius = 30
distance_to_clusters = large_circle_radius + small_circle_radius - central_circle_radius

# Draw the central circle
t.goto(0, -central_circle_radius)
t.pendown()
draw_circle(t, central_circle_radius)
t.penup()

# Draw the clusters
for i in range(8):
    angle = 45 * i
    # Calculate the position for the large circle
    x = distance_to_clusters * math.cos(math.radians(angle))
    y = distance_to_clusters * math.sin(math.radians(angle))
    
    # Draw the large circle
    t.goto(x, y - large_circle_radius)
    t.pendown()
    draw_circle(t, large_circle_radius)
    t.penup()
    
    # Calculate the position for the small circle
    x = (distance_to_clusters - small_circle_radius) * math.cos(math.radians(angle))
    y = (distance_to_clusters - small_circle_radius) * math.sin(math.radians(angle))
    
    # Draw the small circle
    t.goto(x, y - small_circle_radius)
    t.pendown()
    draw_circle(t, small_circle_radius)
    t.penup()

# Hide the turtle and display the result
t.hideturtle()
screen.mainloop()