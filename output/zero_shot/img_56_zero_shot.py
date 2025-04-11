import turtle
import math

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")

# Function to draw a pentagon
def draw_pentagon(size):
    for _ in range(5):
        t.forward(size)
        t.right(72)

# Function to position the turtle
def position_turtle(angle, distance):
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(distance)
    t.pendown()

# Main function to draw the pattern
def draw_pattern():
    num_pentagons = 8
    angle_between = 360 / num_pentagons
    pentagon_size = 100
    distance_to_center = pentagon_size / (2 * math.tan(math.radians(36)))

    for i in range(num_pentagons):
        angle = i * angle_between
        position_turtle(angle, distance_to_center)
        t.setheading(angle + 90)
        draw_pentagon(pentagon_size)

# Draw the pattern
draw_pattern()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()