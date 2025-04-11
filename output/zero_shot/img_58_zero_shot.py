import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")

# Function to draw a semicircle
def draw_semicircle(radius):
    t.circle(radius, 180)

# Draw the pinwheel pattern
for _ in range(8):
    draw_semicircle(100)  # Draw a semicircle with radius 100
    t.right(45)  # Rotate 45 degrees to the right

# Hide the turtle and display the window
t.hideturtle()
turtle.done()