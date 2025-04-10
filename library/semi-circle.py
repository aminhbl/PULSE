import turtle

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
semi_circle_turtle = turtle.Turtle()
semi_circle_turtle.color("black")
semi_circle_turtle.speed(1)

# Function to draw a semi-circle
def draw_semi_circle(radius):
    semi_circle_turtle.penup()
    semi_circle_turtle.goto(-radius, 0)  # Start at the leftmost point of the semi-circle
    semi_circle_turtle.pendown()
    semi_circle_turtle.setheading(90)  # Point upwards
    semi_circle_turtle.circle(radius, 180)  # Draw a semi-circle

# Draw the semi-circle
draw_semi_circle(100)

# Hide the turtle and finish
semi_circle_turtle.hideturtle()
turtle.done()