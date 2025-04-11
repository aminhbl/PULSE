import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Circle and Triangle with Turtle")
screen.bgcolor("white")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(1)
pen.pensize(3)  # Bold black lines

# Draw a small circle on the left
pen.penup()
pen.goto(-100, 0)  # Position for the circle
pen.pendown()
pen.circle(20)  # Small circle with radius 20

# Draw a horizontal line connecting the circle and triangle
pen.penup()
pen.goto(-80, 0)  # Start of the line, slightly right of the circle
pen.pendown()
pen.forward(160)  # Length of the line

# Draw a small triangle on the right
pen.penup()
pen.goto(80, 0)  # Position for the triangle base
pen.pendown()
pen.goto(100, 0)  # Base of the triangle
pen.goto(90, 34.64)  # Top of the triangle (height calculated using Pythagorean theorem)
pen.goto(80, 0)  # Back to the base

# Hide the turtle and finish
pen.hideturtle()
screen.mainloop()