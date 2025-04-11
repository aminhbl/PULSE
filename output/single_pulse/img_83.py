import turtle
import math

# Function to draw a single pentagon
def draw_pentagon(t, side_length):
    for _ in range(5):
        t.forward(side_length)
        t.right(72)

# Setup the turtle
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.color("black")
t.speed(0)  # Fastest speed
t.penup()

# Constants
num_pentagons = 8
side_length = 100
radius = side_length / (2 * math.sin(math.pi / 5))  # Calculate radius of the circumscribed circle
angle_between_pentagons = 360 / num_pentagons

# Draw the pentagons
for i in range(num_pentagons):
    # Calculate the angle for the current pentagon
    angle = i * angle_between_pentagons
    
    # Move to the starting position of the current pentagon
    t.goto(radius * math.cos(math.radians(angle)), radius * math.sin(math.radians(angle)))
    t.setheading(angle + 90)  # Point upwards
    
    # Draw the pentagon
    t.pendown()
    draw_pentagon(t, side_length)
    t.penup()

# Hide the turtle and display the result
t.hideturtle()
screen.mainloop()