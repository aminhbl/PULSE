import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(3)  # Bold black lines

# Function to draw a circle
def draw_circle(x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.circle(radius)

# Parameters
radius = 50
spacing = radius * 1.5  # Overlapping edges

# Draw four interlocking circles
for i in range(4):
    draw_circle(i * spacing, 0, radius)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()