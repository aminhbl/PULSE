import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed

# Function to draw a circle
def draw_circle(radius):
    t.circle(radius)

# Function to draw a cluster
def draw_cluster(large_radius, small_radius):
    # Draw the large circle
    draw_circle(large_radius)
    # Move to the position for the small circle
    t.penup()
    t.goto(t.xcor() + large_radius - small_radius, t.ycor())
    t.pendown()
    # Draw the small circle
    draw_circle(small_radius)
    # Move back to the original position
    t.penup()
    t.goto(t.xcor() - large_radius + small_radius, t.ycor())
    t.pendown()

# Parameters
large_radius = 50
small_radius = 20
center_radius = 20
distance = large_radius + small_radius

# Draw the central small circle
t.penup()
t.goto(0, -center_radius)
t.pendown()
draw_circle(center_radius)

# Draw the eight clusters around the central circle
for i in range(8):
    angle = i * 45  # 360 degrees / 8 clusters = 45 degrees apart
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(distance)
    t.pendown()
    draw_cluster(large_radius, small_radius)

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()