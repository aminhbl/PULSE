import turtle
import math

# Function to draw a heptagon
def draw_heptagon(t, size):
    for _ in range(7):
        t.forward(size)
        t.left(360 / 7)

# Function to draw a line
def draw_line(t, length):
    t.forward(length)

# Setup the turtle
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.color("black")
t.speed(0)  # Fastest speed
t.penup()

# Central point
central_x, central_y = 0, 0
t.goto(central_x, central_y)
t.dot(5, "black")  # Draw the central point

# Heptagon parameters
heptagon_size = 50
angle_between_heptagons = 360 / 6  # 6 heptagons

# Draw the heptagons and lines
for i in range(6):
    # Calculate the position for each heptagon
    angle = math.radians(i * angle_between_heptagons)
    heptagon_x = central_x + math.cos(angle) * (heptagon_size * 1.5)
    heptagon_y = central_y + math.sin(angle) * (heptagon_size * 1.5)
    
    # Move to the starting position of the heptagon
    t.goto(heptagon_x, heptagon_y)
    t.setheading(i * angle_between_heptagons)
    t.pendown()
    
    # Draw the heptagon
    draw_heptagon(t, heptagon_size)
    t.penup()
    
    # Calculate the midpoint of the shared edge
    shared_edge_mid_x = (heptagon_x + t.xcor()) / 2
    shared_edge_mid_y = (heptagon_y + t.ycor()) / 2
    
    # Draw the line from the midpoint to the central point
    t.goto(shared_edge_mid_x, shared_edge_mid_y)
    t.pendown()
    t.goto(central_x, central_y)
    t.penup()

# Hide the turtle and display the result
t.hideturtle()
screen.mainloop()