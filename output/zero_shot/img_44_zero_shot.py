import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.speed(0)
drawer.penup()

# Constants
num_circles = 5
circle_radius = 50
circle_diameter = circle_radius * 2
spacing = 0  # No extra spacing, circles are touching

# Draw the circles
for i in range(num_circles):
    # Move to the starting position for each circle
    drawer.goto(i * (circle_diameter + spacing) - (circle_diameter * (num_circles - 1) / 2), 0)
    drawer.pendown()
    drawer.circle(circle_radius)
    drawer.penup()

# Hide the turtle and display the result
drawer.hideturtle()
screen.mainloop()