import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.color("black")
pen.pensize(2)
pen.speed(1)

# Draw a circle on the left side of the canvas
pen.penup()
pen.goto(-100, 0)
pen.pendown()
pen.circle(50)

# Draw a straight horizontal line starting from the top of the circle
pen.penup()
pen.goto(-100, 50)
pen.pendown()
pen.forward(200)

# Curve the line downward to form the top edge of a semi-circle
pen.right(90)
pen.circle(50, 180)

# Hide the turtle and display the window
pen.hideturtle()
screen.mainloop()
import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(1)

# Draw a circle on the left side of the canvas
t.penup()
t.goto(-100, 0)
t.pendown()
t.circle(50)

# Draw a straight horizontal line starting from the top of the circle
t.penup()
t.goto(-100, 50)
t.pendown()
t.forward(200)

# Draw a semi-circle at the end of the line
t.right(90)
t.circle(50, 180)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()