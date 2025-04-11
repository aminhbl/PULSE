import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.color("black")
pen.pensize(3)
pen.speed(1)

# Draw a small circle on the left
pen.penup()
pen.goto(-100, 0)  # Position the turtle to the left
pen.pendown()
pen.circle(20)  # Draw a circle with radius 20

# Draw a short horizontal line on the right
pen.penup()
pen.goto(50, 0)  # Position the turtle to the right
pen.pendown()
pen.forward(40)  # Draw a horizontal line

# Hide the turtle and finish
pen.hideturtle()
screen.mainloop()