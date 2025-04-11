import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(0)  # Fastest speed
pen.penup()

# Constants
num_circles = 8
radius = 20
distance_from_center = 100

# Draw circles
for i in range(num_circles):
    angle = 360 / num_circles * i
    pen.goto(distance_from_center * turtle.cos(turtle.radians(angle)),
             distance_from_center * turtle.sin(turtle.radians(angle)))
    pen.pendown()
    pen.circle(radius)
    pen.penup()

# Hide the turtle and display the window
pen.hideturtle()
screen.mainloop()