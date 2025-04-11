import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")

# Function to draw a circle
def draw_circle(radius):
    t.circle(radius)

# Draw six overlapping circles
num_circles = 6
radius = 100
angle = 360 / num_circles

for _ in range(num_circles):
    draw_circle(radius)
    t.right(angle)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()