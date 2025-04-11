import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(1)

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        pen.forward(size)
        pen.right(90)

# Function to draw a line and a square at the end
def draw_line_and_square(angle, length, square_size):
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(angle)
    pen.pendown()
    pen.forward(length)
    draw_square(square_size)

# Draw the Y-shaped structure with squares at the ends
line_length = 100
square_size = 30

# Draw the first line and square
draw_line_and_square(90, line_length, square_size)

# Draw the second line and square
draw_line_and_square(210, line_length, square_size)

# Draw the third line and square
draw_line_and_square(330, line_length, square_size)

# Hide the turtle and display the window
pen.hideturtle()
screen.mainloop()