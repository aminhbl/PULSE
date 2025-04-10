import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.speed(0)
drawer.pensize(3)

# Function to draw a circle
def draw_circle(t, x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.circle(radius)

# Function to draw a pentagon
def draw_pentagon(t, x, y, side_length):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(5):
        t.forward(side_length)
        t.right(72)

# Function to draw a line
def draw_line(t, x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)

# Draw a circle on the left side
circle_radius = 50
circle_x = -150
circle_y = 0
draw_circle(drawer, circle_x, circle_y, circle_radius)

# Draw a pentagon on the right side
pentagon_side_length = 100
pentagon_x = 50
pentagon_y = -circle_radius
draw_pentagon(drawer, pentagon_x, pentagon_y, pentagon_side_length)

# Draw a line connecting the base of the circle to the base of the pentagon
line_x1 = circle_x
line_y1 = -circle_radius
line_x2 = pentagon_x
line_y2 = -circle_radius
draw_line(drawer, line_x1, line_y1, line_x2, line_y2)

# Hide the turtle and display the window
drawer.hideturtle()
screen.mainloop()