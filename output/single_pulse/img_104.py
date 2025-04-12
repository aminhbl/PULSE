import turtle
import math

# Function to draw a circle
def draw_circle(t, radius):
    t.penup()
    t.forward(radius)
    t.left(90)
    t.pendown()
    t.circle(radius)
    t.penup()
    t.right(90)
    t.backward(radius)
    t.pendown()

# Function to draw an equilateral triangle
def draw_triangle(t, side_length):
    for _ in range(3):
        t.forward(side_length)
        t.left(120)

# Function to draw a line
def draw_line(t, length):
    t.forward(length)

# Setup the turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.color("black")

# Constants
num_circles = 6
circle_radius = 50
triangle_side = 50
distance_from_center = 100

# Draw central point
t.penup()
t.goto(0, 0)
t.dot(5, "black")

# Draw circles and triangles
angle_between_circles = 360 / num_circles

for i in range(num_circles):
    # Calculate position for each circle
    angle = math.radians(i * angle_between_circles)
    x = distance_from_center * math.cos(angle)
    y = distance_from_center * math.sin(angle)
    
    # Move to circle position
    t.penup()
    t.goto(x, y - circle_radius)
    t.pendown()
    
    # Draw circle
    draw_circle(t, circle_radius)
    
    # Move to triangle start position
    t.penup()
    t.goto(x, y)
    t.setheading(i * angle_between_circles - 90)
    t.forward(circle_radius - triangle_side / (2 * math.sqrt(3)))
    t.pendown()
    
    # Draw triangle
    draw_triangle(t, triangle_side)
    
    # Draw line from triangle base midpoint to circle edge
    t.penup()
    t.goto(x, y)
    t.setheading(i * angle_between_circles - 90)
    t.forward(circle_radius)
    t.pendown()
    t.setheading(i * angle_between_circles)
    draw_line(t, triangle_side / (2 * math.sqrt(3)))

# Hide turtle and display window
t.hideturtle()
screen.mainloop()