import turtle
import math

# Function to draw a heptagon
def draw_heptagon(t, size):
    angle = 360 / 7
    for _ in range(7):
        t.forward(size)
        t.left(angle)

# Setup the turtle
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.penup()

# Constants
num_heptagons = 6
heptagon_size = 100
center_distance = heptagon_size * math.cos(math.radians(360 / 14))  # Distance from center to a heptagon's center

# Draw the flower-like pattern
for i in range(num_heptagons):
    angle = i * (360 / num_heptagons)
    t.goto(center_distance * math.cos(math.radians(angle)), center_distance * math.sin(math.radians(angle)))
    t.setheading(angle + 90)
    t.pendown()
    draw_heptagon(t, heptagon_size)
    t.penup()

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()