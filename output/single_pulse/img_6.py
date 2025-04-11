import turtle

# Function to draw a circle with a given radius and center position
def draw_circle(t, radius, center_x, center_y):
    t.penup()
    t.goto(center_x, center_y - radius)
    t.pendown()
    t.circle(radius)

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
turtle.bgcolor("white")
t.color("black")

# Base point
base_x = 0
base_y = 0

# Radii of the circles
radii = [20, 40, 60, 80, 100]

# Draw the circles
for i, radius in enumerate(radii):
    center_y = base_y + radius
    draw_circle(t, radius, base_x, center_y)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()