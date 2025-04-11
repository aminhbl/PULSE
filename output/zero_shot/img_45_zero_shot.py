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

# Initial position
start_x = -150
y = 0
radius = 50
spacing = 30  # Overlapping spacing

# Draw six hollow circles
for i in range(6):
    draw_hollow_circle(start_x + i * (2 * radius - spacing), y, radius)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()