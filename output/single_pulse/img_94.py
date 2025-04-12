import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")
t.color("black")

# Function to draw a line
def draw_line(length):
    t.penup()
    t.forward(length)
    t.pendown()
    t.backward(length)

# Function to draw a circle
def draw_circle(radius):
    t.penup()
    t.forward(radius)
    t.pendown()
    t.circle(radius)
    t.penup()
    t.backward(radius)

# Main function to draw the snowflake
def draw_snowflake():
    num_arms = 3
    angle_between_arms = 360 / num_arms
    line_length = 100
    circle_radius = 10
    gap = 20

    for _ in range(num_arms):
        t.penup()
        t.goto(0, 0)
        t.setheading(0)
        t.left(angle_between_arms * _)
        t.forward(gap)
        draw_line(line_length - gap)
        t.forward(line_length - gap + circle_radius)
        draw_circle(circle_radius)
        t.backward(line_length - gap + circle_radius)

# Draw the snowflake
draw_snowflake()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()