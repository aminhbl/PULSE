import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle to draw the circles
drawer = turtle.Turtle()
drawer.color("black")
drawer.speed(0)  # Fastest drawing speed

# Constants
num_circles = 8
angle_between_circles = 360 / num_circles
circle_radius = 50
formation_radius = 150

# Function to draw a circle at a specific position
def draw_circle(x, y, radius):
    drawer.penup()
    drawer.goto(x, y - radius)  # Move to the starting point of the circle
    drawer.pendown()
    drawer.circle(radius)
    drawer.penup()

# Draw the circular formation of circles
for i in range(num_circles):
    angle = math.radians(i * angle_between_circles)
    x = formation_radius * math.cos(angle)
    y = formation_radius * math.sin(angle)
    draw_circle(x, y, circle_radius)

# Hide the turtle and display the result
drawer.hideturtle()
screen.mainloop()