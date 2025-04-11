import turtle

# Setup the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")

# Function to draw a circle with a bold black outline
def draw_circle(t, x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.pensize(3)
    t.pencolor("black")
    t.circle(radius)

# Function to draw a pentagon with a bold black outline
def draw_pentagon(t, x, y, side_length):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pensize(3)
    t.pencolor("black")
    angle = 72
    for _ in range(5):
        t.forward(side_length)
        t.right(angle)

# Function to draw a horizontal line
def draw_line(t, x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.pensize(3)
    t.pencolor("black")
    t.goto(x2, y2)

# Create a turtle object
t = turtle.Turtle()
t.speed(0)

# Draw the circle on the left side
circle_radius = 50
circle_x = -200
circle_y = 0
draw_circle(t, circle_x, circle_y, circle_radius)

# Draw the pentagon on the right side
pentagon_side_length = 100
pentagon_x = 100
pentagon_y = -circle_radius
draw_pentagon(t, pentagon_x, pentagon_y, pentagon_side_length)

# Draw the horizontal line connecting the base of the circle and the pentagon
line_x1 = circle_x
line_y1 = -circle_radius
line_x2 = pentagon_x
line_y2 = -circle_radius
draw_line(t, line_x1, line_y1, line_x2, line_y2)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()