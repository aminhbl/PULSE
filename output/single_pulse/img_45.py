import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("white")

# Function to draw a circle with a black outline and white fill
def draw_circle(radius):
    t.fillcolor("white")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw six circles in a row
radius = 50
spacing = 2 * radius  # Circles are touching each other

t.penup()
t.goto(-3 * spacing + radius, 0)  # Start position for the first circle
t.pendown()

for _ in range(6):
    draw_circle(radius)
    t.penup()
    t.forward(spacing)
    t.pendown()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()