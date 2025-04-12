import turtle
import math

# Function to draw a pentagon
def draw_pentagon(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(72)

# Function to draw a square
def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Function to draw a cluster of a pentagon and a rotated square
def draw_cluster(t, size, square_angle):
    # Draw pentagon
    draw_pentagon(t, size)
    # Rotate and draw square
    t.right(square_angle)
    draw_square(t, size)
    t.left(square_angle)  # Reset orientation

# Function to draw the entire pattern
def draw_pattern(t, size, num_clusters):
    angle_between_clusters = 360 / num_clusters
    square_angles = [0, 15, 30, 45, 60]  # Different angles for square rotation

    for i in range(num_clusters):
        draw_cluster(t, size, square_angles[i % len(square_angles)])
        t.penup()
        t.forward(size * 2)  # Move to the next cluster position
        t.right(angle_between_clusters)
        t.pendown()

# Setup turtle
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.color("black")

# Calculate size based on desired pattern size
size = 50

# Draw the pattern
draw_pattern(t, size, 5)

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()