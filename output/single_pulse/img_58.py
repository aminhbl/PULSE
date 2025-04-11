import turtle

# Function to draw a semi-circle
def draw_semi_circle(t, radius):
    t.circle(radius, 180)  # Draw a semi-circle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")  # Background color

# Central point coordinates
center_x, center_y = 0, 0

# Move the turtle to the starting position
t.penup()
t.goto(center_x, center_y)
t.pendown()

# Draw 8 semi-circles rotated by 45 degrees each
for _ in range(8):
    draw_semi_circle(t, 100)  # Draw a semi-circle with radius 100
    t.right(45)  # Rotate 45 degrees

# Hide the turtle and display the window
t.hideturtle()
turtle.done()