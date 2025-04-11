import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.pensize(3)  # Bold black lines
pen.color("black")
pen.speed(1)

# Draw the small circle on the left
pen.penup()
pen.goto(-100, 0)
pen.pendown()
pen.circle(20)  # Small circle with radius 20

# Draw the horizontal line connecting the bases
pen.penup()
pen.goto(-80, 0)
pen.pendown()
pen.forward(160)  # Line length is the distance between the circle and semicircle

# Draw the larger semicircle on the right
pen.penup()
pen.goto(80, 0)
pen.setheading(90)  # Face upwards to start semicircle
pen.pendown()
pen.circle(60, 180)  # Semicircle with radius 60, 180 degrees

# Hide the turtle and finish
pen.hideturtle()
screen.mainloop()