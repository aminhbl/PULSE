import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.speed(0)  # Fastest drawing speed

# Function to draw a circle at a given position
def draw_circle(x, y, radius):
    drawer.penup()
    drawer.goto(x, y - radius)  # Move to the bottom of the circle
    drawer.pendown()
    drawer.circle(radius)

# Calculate positions for the circles
radius = 50
distance = radius * 2 * 1.5  # Distance between centers of circles

# Bottom circle
bottom_x = 0
bottom_y = -distance / (2 * 3**0.5)
draw_circle(bottom_x, bottom_y, radius)

# Top left circle
top_left_x = -distance / 2
top_left_y = distance / (2 * 3**0.5)
draw_circle(top_left_x, top_left_y, radius)

# Top right circle
top_right_x = distance / 2
top_right_y = distance / (2 * 3**0.5)
draw_circle(top_right_x, top_right_y, radius)

# Hide the turtle and display the window
drawer.hideturtle()
screen.mainloop()