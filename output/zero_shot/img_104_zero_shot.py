import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed

# Function to draw a circle with a triangle inside
def draw_circle_with_triangle(radius, angle):
    # Move to the starting point of the circle
    t.penup()
    t.goto(radius * math.cos(math.radians(angle)), radius * math.sin(math.radians(angle)))
    t.pendown()
    
    # Draw the circle
    t.circle(radius)
    
    # Calculate the triangle vertices
    triangle_side = radius * math.sqrt(3)
    t.penup()
    t.goto(radius * math.cos(math.radians(angle)), radius * math.sin(math.radians(angle)))
    t.pendown()
    
    # Draw the triangle
    t.setheading(angle + 90)
    t.forward(triangle_side / 2)
    t.right(120)
    t.forward(triangle_side)
    t.right(120)
    t.forward(triangle_side)
    t.right(120)
    t.forward(triangle_side / 2)
    
    # Draw the line connecting the triangle base to the circle's edge
    t.penup()
    t.goto(radius * math.cos(math.radians(angle)), radius * math.sin(math.radians(angle)))
    t.pendown()
    t.setheading(angle + 90)
    t.forward(radius)

# Parameters
num_circles = 6
circle_radius = 50
distance_from_center = 150

# Draw the circles with triangles
for i in range(num_circles):
    angle = i * (360 / num_circles)
    draw_circle_with_triangle(circle_radius, angle)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()