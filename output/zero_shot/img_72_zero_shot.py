import turtle
import math

# Function to draw a heptagon
def draw_heptagon(t, size):
    for _ in range(7):
        t.forward(size)
        t.left(360 / 7)

# Function to move the turtle to a specific position without drawing
def move_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.speed(0)

# Define the size of the heptagon and the length of the connecting lines
heptagon_size = 50
line_length = 100

# Calculate the angle for the Y-shape
angle = 120

# Draw the Y-shaped structure with heptagons at the ends
for i in range(3):
    # Draw the connecting line
    t.forward(line_length)
    
    # Draw the heptagon
    draw_heptagon(t, heptagon_size)
    
    # Move back to the center
    t.penup()
    t.backward(line_length)
    t.pendown()
    
    # Rotate for the next arm of the Y
    t.left(angle)

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()