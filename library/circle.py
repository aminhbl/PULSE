import turtle

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
circle_turtle = turtle.Turtle()
circle_turtle.color("black")
circle_turtle.speed(1)  # Set the speed of the turtle

# Draw a circle
radius = 100  # Radius of the circle
circle_turtle.penup()
circle_turtle.goto(0, -radius)  # Move the turtle to the starting position
circle_turtle.pendown()
circle_turtle.circle(radius)

# Hide the turtle and finish
circle_turtle.hideturtle()
turtle.done()