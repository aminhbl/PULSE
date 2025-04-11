import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(1)
t.pensize(3)  # Bold black line

# Function to draw a semicircle facing left
def draw_semicircle(radius):
    t.circle(radius, 180)  # Draw a semicircle

# Position the turtle for the first semicircle
t.penup()
t.goto(-150, 0)
t.pendown()

# Draw three semicircles
for _ in range(3):
    draw_semicircle(50)  # Draw a semicircle with radius 50
    t.penup()
    t.forward(100)  # Move to the next position
    t.pendown()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()