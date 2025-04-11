import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
pen = turtle.Turtle()
pen.speed(0)  # Fastest speed
pen.hideturtle()

# Function to draw a circle at a given position
def draw_circle(x, y, radius):
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.circle(radius)

# Function to draw a line from the center to a given point
def draw_line(x, y):
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.goto(x, y)

# Number of circles
num_circles = 6
radius = 50
distance_from_center = 100

# Draw the circles and lines
for i in range(num_circles):
    angle = 2 * math.pi / num_circles * i
    x = distance_from_center * math.cos(angle)
    y = distance_from_center * math.sin(angle)
    
    draw_circle(x, y, radius)
    draw_line(x, y)

# Hide the turtle and display the window
pen.hideturtle()
screen.mainloop()