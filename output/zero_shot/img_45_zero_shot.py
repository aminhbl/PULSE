import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("white")

# Function to draw a circle with a black outline and white fill
def draw_circle(x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color("black", "white")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Parameters
radius = 50
spacing = 2 * radius

# Draw six circles in a row
for i in range(6):
    draw_circle(i * spacing, 0, radius)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()