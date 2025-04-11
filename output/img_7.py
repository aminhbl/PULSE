import turtle

# Function to draw a circle with a given radius and center position
def draw_circle(t, radius, center_y):
    t.penup()
    t.goto(0, center_y - radius)  # Move to the bottom of the circle
    t.pendown()
    t.circle(radius)

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
t.hideturtle()

# Base point (0, 0)
base_y = 0

# Radii of the circles
radii = [50, 100, 150, 200]

# Draw the circles
for i, radius in enumerate(radii):
    center_y = base_y + radius  # Calculate the center y position
    draw_circle(t, radius, center_y)

# Finish
turtle.done()