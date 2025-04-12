import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")

# Function to draw a hollow circle
def draw_hollow_circle(radius):
    t.penup()
    t.forward(radius)
    t.left(90)
    t.pendown()
    t.circle(radius)
    t.penup()
    t.right(90)
    t.backward(radius)
    t.pendown()

# Number of circles
num_circles = 7
# Radius of each small circle
small_circle_radius = 20
# Radius of the large circle on which small circles are placed
large_circle_radius = 100

# Draw the circles
for i in range(num_circles):
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.left(i * (360 / num_circles))
    t.forward(large_circle_radius)
    t.pendown()
    draw_hollow_circle(small_circle_radius)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()