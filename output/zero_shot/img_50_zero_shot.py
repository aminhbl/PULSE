import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(3)  # Bold black lines

# Function to draw a semicircle facing left
def draw_semicircle(radius):
    t.circle(radius, 180)

# Number of semicircles
num_semicircles = 6

# Radius of each semicircle
radius = 50

# Spacing between semicircles
spacing = 20

# Initial position
t.penup()
t.goto(-((num_semicircles - 1) * (radius + spacing) / 2), 0)
t.pendown()

# Draw the semicircles
for _ in range(num_semicircles):
    draw_semicircle(radius)
    t.penup()
    t.forward(radius + spacing)
    t.pendown()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()