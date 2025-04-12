import turtle
import math

# Function to draw a pentagon
def draw_pentagon(t, side_length):
    for _ in range(5):
        t.forward(side_length)
        t.right(72)

# Function to draw an arc
def draw_arc(t, radius, extent):
    t.circle(radius, extent)

# Setup the turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.color("black")
t.speed(0)  # Fastest speed

# Constants
num_pentagons = 8
side_length = 100
angle_between_pentagons = 360 / num_pentagons
arc_radius = side_length / (2 * math.sin(math.radians(36)))  # Calculate radius for the arc
arc_extent = 72  # Arc extent to match the pentagon's angle

# Draw the circular pattern of pentagons
for i in range(num_pentagons):
    # Draw a pentagon
    draw_pentagon(t, side_length)
    
    # Position turtle for the arc
    t.penup()
    t.forward(side_length)
    t.right(108)  # Align for the arc
    t.pendown()
    
    # Draw the inward-facing arc
    draw_arc(t, arc_radius, arc_extent)
    
    # Reposition for the next pentagon
    t.penup()
    t.left(180 - angle_between_pentagons)
    t.forward(side_length)
    t.right(180 - angle_between_pentagons)
    t.pendown()

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()