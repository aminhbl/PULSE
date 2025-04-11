import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Function to draw a circle
def draw_circle(t, radius):
    t.circle(radius)

# Function to draw a semicircle
def draw_semicircle(t, radius):
    t.circle(radius, 180)

# Function to position the turtle without drawing
def move_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Constants
small_circle_radius = 20
large_circle_radius = small_circle_radius * 2
hexagon_side = small_circle_radius * math.sqrt(3)

# Draw the small circles in a hexagonal ring
for i in range(6):
    angle = math.radians(60 * i)
    x = hexagon_side * math.cos(angle)
    y = hexagon_side * math.sin(angle)
    move_to(pen, x, y - small_circle_radius)
    draw_circle(pen, small_circle_radius)

# Draw the surrounding semicircles
for i in range(6):
    angle = math.radians(60 * i + 30)
    x = (hexagon_side + small_circle_radius) * math.cos(angle)
    y = (hexagon_side + small_circle_radius) * math.sin(angle)
    move_to(pen, x, y)
    pen.setheading(60 * i + 90)
    draw_semicircle(pen, large_circle_radius)

# Hide the turtle and display the result
pen.hideturtle()
screen.mainloop()