import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("white")

# Function to draw a circle with a bold black outline
def draw_circle():
    t.penup()
    t.goto(-150, 0)  # Position the turtle to the left side
    t.pendown()
    t.pensize(3)  # Bold outline
    t.pencolor("black")
    t.circle(50)  # Draw circle with radius 50

# Function to draw a nonagon with a bold black outline
def draw_nonagon():
    t.penup()
    t.goto(50, 0)  # Position the turtle to the right side
    t.pendown()
    t.pensize(3)  # Bold outline
    t.pencolor("black")
    side_length = 70  # Side length for the nonagon
    for _ in range(9):
        t.forward(side_length)
        t.left(40)  # 360/9 = 40 degrees

# Draw the circle
draw_circle()

# Draw the nonagon
draw_nonagon()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()