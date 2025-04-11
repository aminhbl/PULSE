import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
pen = turtle.Turtle()
pen.speed(0)  # Fastest speed
pen.penup()

# Constants
num_circles = 8
radius = 50  # Radius of each circle
distance = 2 * radius  # Distance from the center to the center of each circle
angle_between = 360 / num_circles  # Angle between each circle

# Draw circles
for i in range(num_circles):
    # Calculate the position for each circle
    angle = math.radians(angle_between * i)
    x = distance * math.cos(angle)
    y = distance * math.sin(angle)
    
    # Move the turtle to the starting position of the circle
    pen.goto(x, y - radius)
    pen.pendown()
    
    # Draw the circle
    pen.circle(radius)
    pen.penup()

# Hide the turtle and display the result
pen.hideturtle()
screen.mainloop()