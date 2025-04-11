import turtle

# Function to draw a circle
def draw_circle(x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.circle(radius)

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()

# Define the radius of the circles
radius = 50

# Calculate the positions for the circles
# The height of an equilateral triangle with side length s is (sqrt(3)/2) * s
# We want the centers of the circles to form an equilateral triangle
side_length = 3 * radius  # Arbitrary choice to ensure non-overlapping
height = (3**0.5 / 2) * side_length

# Bottom circle
bottom_x = 0
bottom_y = -height / 3

# Top left circle
top_left_x = -side_length / 2
top_left_y = height * 2 / 3

# Top right circle
top_right_x = side_length / 2
top_right_y = height * 2 / 3

# Draw the circles
draw_circle(bottom_x, bottom_y, radius)
draw_circle(top_left_x, top_left_y, radius)
draw_circle(top_right_x, top_right_y, radius)

# Finish
turtle.done()