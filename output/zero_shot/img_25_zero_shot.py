import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(1)
pen.pensize(3)
pen.color("black")

# Draw the smaller semicircle on the left
pen.penup()
pen.goto(-100, 50)  # Position the turtle
pen.pendown()
pen.setheading(90)  # Face upwards
pen.circle(50, 180)  # Draw a semicircle with radius 50

# Draw the larger semicircle on the right
pen.penup()
pen.goto(100, 0)  # Position the turtle
pen.pendown()
pen.setheading(90)  # Face upwards
pen.circle(100, 180)  # Draw a semicircle with radius 100

# Hide the turtle and display the window
pen.hideturtle()
screen.mainloop()