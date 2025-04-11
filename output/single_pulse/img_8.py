import turtle

# Function to draw a circle with a given radius and center
def draw_circle(t, radius, center_x, center_y):
    t.penup()
    t.goto(center_x, center_y - radius)
    t.pendown()
    t.circle(radius)

# Setup the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
turtle.bgcolor("white")
t.color("black")

# Base point
base_x = 0
base_y = 0

# Number of circles
num_circles = 6

# Initial radius and increment
initial_radius = 20
radius_increment = 20

# Draw circles
for i in range(num_circles):
    radius = initial_radius + i * radius_increment
    center_y = base_y + radius
    draw_circle(t, radius, base_x, center_y)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()