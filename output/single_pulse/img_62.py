import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")

# Function to draw a line at a specific angle
def draw_line(angle):
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.pendown()
    t.forward(100)
    t.penup()
    t.goto(0, 0)
    t.setheading(angle + 180)
    t.pendown()
    t.forward(100)

# Draw lines at specified angles
angles = [90, 0, 45, 135, 135 + 90, 45 + 90, 45, 135]
for angle in angles:
    draw_line(angle)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()