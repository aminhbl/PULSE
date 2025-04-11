import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")

# Function to draw a line
def draw_line(length):
    t.forward(length)

# Function to draw a circle
def draw_circle(radius):
    t.circle(radius)

# Central point coordinates
center_x, center_y = 0, 0

# Number of lines and angle between them
num_lines = 7
angle_between_lines = 360 / num_lines

# Length of each line and radius of each circle
line_length = 100
circle_radius = 20

# Move to the central point
t.penup()
t.goto(center_x, center_y)
t.pendown()

# Draw the pattern
for _ in range(num_lines):
    draw_line(line_length)
    draw_circle(circle_radius)
    t.penup()
    t.goto(center_x, center_y)
    t.pendown()
    t.right(angle_between_lines)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()