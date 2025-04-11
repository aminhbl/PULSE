import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")

# Function to draw a circle
def draw_circle(radius):
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.circle(radius)

# Draw the central circle
draw_circle(50)

# Draw four additional circles in a radial pattern
for angle in [0, 90, 180, 270]:
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(50)
    t.pendown()
    draw_circle(50)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()