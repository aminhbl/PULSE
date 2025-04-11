import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing the circle
circle_turtle = turtle.Turtle()
circle_turtle.penup()
circle_turtle.goto(-150, 0)  # Move to the left side of the canvas
circle_turtle.pendown()
circle_turtle.pensize(3)  # Bold black line
circle_turtle.circle(50)  # Draw a circle with radius 50

# Create a turtle for drawing the line
line_turtle = turtle.Turtle()
line_turtle.penup()
line_turtle.goto(50, 0)  # Move to the right side of the canvas
line_turtle.pendown()
line_turtle.pensize(3)  # Bold black line
line_turtle.forward(100)  # Draw a horizontal line

# Hide the turtles
circle_turtle.hideturtle()
line_turtle.hideturtle()

# Keep the window open
turtle.done()