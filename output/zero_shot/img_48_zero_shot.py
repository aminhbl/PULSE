import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(1)  # Set the speed of the turtle

# Function to draw a circle
def draw_circle(x, y, radius):
    t.penup()
    t.goto(x, y - radius)  # Move to the starting point of the circle
    t.pendown()
    t.circle(radius)
    t.penup()

# Draw three hollow black circles with overlapping edges
radius = 50
spacing = 30  # Overlapping space between circles

# First circle
draw_circle(-radius - spacing, 0, radius)

# Second circle
draw_circle(0, 0, radius)

# Third circle
draw_circle(radius + spacing, 0, radius)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()