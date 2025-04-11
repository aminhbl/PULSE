import turtle

# Set up the turtle
turtle.speed(0)
turtle.penup()
turtle.hideturtle()

# Function to draw a circle with a black border and white background
def draw_circle(x, y, radius):
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("white")
    turtle.pencolor("black")
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()

# Parameters
radius = 50
spacing = 2 * radius

# Draw five circles in a horizontal row
for i in range(5):
    draw_circle(i * spacing, 0, radius)

# Finish
turtle.done()