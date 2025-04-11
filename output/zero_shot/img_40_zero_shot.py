import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(3)

# Function to draw a semicircle facing left
def draw_semicircle(radius):
    t.setheading(90)  # Face upwards
    t.circle(radius, 180)  # Draw a semicircle

# Main function to draw six semicircles
def draw_pattern():
    radius = 50
    spacing = 20
    for _ in range(6):
        draw_semicircle(radius)
        t.penup()
        t.forward(radius * 2 + spacing)
        t.pendown()

# Position the turtle
t.penup()
t.goto(-200, 0)
t.pendown()

# Draw the pattern
draw_pattern()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()