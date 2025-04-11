import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.speed(0)  # Fastest drawing speed
drawer.penup()

# Function to draw a circle with a given radius and bottom point
def draw_circle_with_bottom_point(radius, bottom_x, bottom_y):
    # Calculate the center of the circle
    center_y = bottom_y + radius
    # Move the turtle to the starting point of the circle
    drawer.goto(bottom_x, center_y - radius)
    drawer.pendown()
    # Draw the circle
    drawer.circle(radius)
    drawer.penup()

# Bottom point coordinates
bottom_x = 0
bottom_y = -200

# Radii of the circles
radii = [50, 100, 150]

# Draw the nested circles
for radius in radii:
    draw_circle_with_bottom_point(radius, bottom_x, bottom_y)

# Hide the turtle and finish
drawer.hideturtle()
screen.mainloop()