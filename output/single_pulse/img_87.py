import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")
t.color("black")

# Function to draw a line
def draw_line(length):
    t.penup()
    t.forward(20)  # Small gap from the center
    t.pendown()
    t.forward(length)
    t.penup()
    t.backward(length + 20)  # Return to the center

# Function to draw a circle at the end of a line
def draw_circle(radius):
    t.penup()
    t.forward(radius)
    t.pendown()
    t.circle(radius)
    t.penup()
    t.backward(radius)

# Main function to draw the snowflake
def draw_snowflake():
    num_arms = 5
    angle = 360 / num_arms
    line_length = 100
    circle_radius = 10

    for _ in range(num_arms):
        draw_line(line_length)
        draw_circle(circle_radius)
        t.right(angle)

# Move the turtle to the starting position
t.penup()
t.goto(0, 0)
t.pendown()

# Draw the snowflake
draw_snowflake()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()