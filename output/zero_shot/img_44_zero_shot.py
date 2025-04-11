import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")

# Function to draw a hollow circle
def draw_hollow_circle(x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.circle(radius)
    t.penup()

# Parameters
radius = 50
spacing = 20  # Overlapping edges

# Draw five hollow circles
start_x = -2 * (radius + spacing)
for i in range(5):
    draw_hollow_circle(start_x + i * (2 * radius + spacing), 0, radius)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()