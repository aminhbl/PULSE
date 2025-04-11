import turtle
import math

# Function to draw a heptagon
def draw_heptagon(t, size):
    for _ in range(7):
        t.forward(size)
        t.left(360 / 7)

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.color("black")
t.speed(0)  # Fastest speed
t.penup()

# Center point of the canvas
center_x, center_y = 0, 0

# Radius of the circle for heptagon placement
radius = 150

# Number of heptagons
num_heptagons = 8

# Angle between each heptagon
angle_between = 360 / num_heptagons

# Size of each heptagon
heptagon_size = 50

# Draw the heptagons
for i in range(num_heptagons):
    # Calculate the angle for the current heptagon
    angle = angle_between * i
    
    # Calculate the position for the current heptagon
    x = center_x + radius * math.cos(math.radians(angle))
    y = center_y + radius * math.sin(math.radians(angle))
    
    # Move the turtle to the starting position
    t.goto(x, y)
    t.setheading(angle + 90)  # Rotate the heptagon slightly
    
    # Draw the heptagon
    t.pendown()
    draw_heptagon(t, heptagon_size)
    t.penup()

# Hide the turtle and display the result
t.hideturtle()
screen.mainloop()