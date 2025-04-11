import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Circle and Semicircle with Connecting Line")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(1)

# Draw the circle on the left
pen.penup()
pen.goto(-100, 0)
pen.pendown()
pen.circle(50)

# Draw the horizontal line connecting the circle and semicircle
pen.penup()
pen.goto(-100, 50)
pen.pendown()
pen.forward(200)

# Draw the semicircle on the right
pen.right(90)
pen.circle(50, 180)

# Hide the turtle
pen.hideturtle()

# Finish
screen.mainloop()