import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
flower_turtle = turtle.Turtle()
flower_turtle.speed(0)  # Fastest speed

# Function to draw a heptagon
def draw_heptagon(t, side_length):
    angle = 360 / 7
    for _ in range(7):
        t.forward(side_length)
        t.right(angle)

# Function to draw the flower-like pattern
def draw_flower(t, num_heptagons, side_length):
    angle_between_heptagons = 360 / num_heptagons
    for _ in range(num_heptagons):
        draw_heptagon(t, side_length)
        t.penup()
        t.forward(side_length * 2)  # Move to the next position
        t.pendown()
        t.right(angle_between_heptagons)

# Calculate the side length of the heptagon
# This is an arbitrary choice to make the pattern look nice
side_length = 50

# Draw the flower pattern
draw_flower(flower_turtle, 8, side_length)

# Hide the turtle and display the window
flower_turtle.hideturtle()
screen.mainloop()