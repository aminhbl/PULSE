import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(0)

# Function to draw a circle at a given position
def draw_circle(x, y, radius):
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.circle(radius)

# Function to draw a line from the center to a given position
def draw_line(x, y):
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.goto(x, y)

# Draw the Y-shaped structure
pen.penup()
pen.goto(0, 0)
pen.setheading(90)  # Point upwards
pen.pendown()
pen.forward(100)  # Central line

# Draw the left branch
pen.backward(50)
pen.left(45)
pen.forward(70)

# Draw the right branch
pen.backward(70)
pen.right(90)
pen.forward(70)

# Draw circles at the ends of the Y-shaped structure
pen.penup()
pen.goto(0, 100)
pen.setheading(90)
pen.forward(20)
draw_circle(pen.xcor(), pen.ycor(), 20)

pen.goto(-50, 50)
pen.setheading(135)
pen.forward(20)
draw_circle(pen.xcor(), pen.ycor(), 20)

pen.goto(50, 50)
pen.setheading(45)
pen.forward(20)
draw_circle(pen.xcor(), pen.ycor(), 20)

# Hide the turtle and display the window
pen.hideturtle()
screen.mainloop()