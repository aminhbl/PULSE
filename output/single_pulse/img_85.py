import turtle

# Function to draw a circle with a given radius
def draw_circle(radius):
    turtle.penup()
    turtle.goto(0, -radius)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

# Function to draw a small hollow circle at a specific position
def draw_small_circle(radius, angle, small_radius):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(angle)
    turtle.forward(radius)
    turtle.pendown()
    turtle.circle(small_radius)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

# Setup the turtle
turtle.speed(0)
turtle.hideturtle()

# Parameters
large_radius = 200
small_radius = 20
num_circles = 7

# Draw the large guiding circle
draw_circle(large_radius)

# Draw the small hollow circles
for i in range(num_circles):
    angle = 360 / num_circles * i
    draw_small_circle(large_radius, angle, small_radius)

# Remove the large guiding circle by clearing the screen and redrawing the small circles
turtle.clear()

# Redraw the small hollow circles
for i in range(num_circles):
    angle = 360 / num_circles * i
    draw_small_circle(large_radius, angle, small_radius)

# Finish
turtle.done()