import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")

# Function to draw a circle with a given radius and center position
def draw_circle(radius, center_x, center_y):
    t.penup()
    t.goto(center_x, center_y - radius)  # Move to the bottom of the circle
    t.pendown()
    t.circle(radius)

# Base point (x, y)
base_x = 0
base_y = -200

# Radii of the circles
radius1 = 50
radius2 = 100
radius3 = 150

# Draw the smallest circle
draw_circle(radius1, base_x, base_y + radius1)

# Draw the second circle
draw_circle(radius2, base_x, base_y + radius2)

# Draw the largest circle
draw_circle(radius3, base_x, base_y + radius3)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()