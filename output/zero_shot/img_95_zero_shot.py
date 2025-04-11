import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.bgcolor("white")

# Function to draw a single arm of the snowflake
def draw_arm():
    t.penup()
    t.forward(20)  # Short space
    t.pendown()
    t.forward(30)  # Short line
    t.penup()
    t.forward(20)  # Short space
    t.pendown()
    t.circle(10)   # Small circle at the end
    t.penup()
    t.backward(70) # Move back to the center

# Draw the seven-sided snowflake pattern
for _ in range(7):
    draw_arm()
    t.right(360 / 7)  # Turn to the next arm

# Hide the turtle and display the window
t.hideturtle()
turtle.done()