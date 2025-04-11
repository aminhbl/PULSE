import turtle

# Setup the screen
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

# Function to draw a triangle
def draw_triangle(t, x, y, side_length):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(3):
        t.forward(side_length)
        t.left(120)

# Function to draw a line
def draw_line(t, x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)

# Draw the circle on the left
circle_radius = 50
circle_x = -150
circle_y = 0
draw_circle(drawer, circle_x, circle_y, circle_radius)

# Draw the triangle on the right
triangle_side = 100
triangle_x = 100
triangle_y = -triangle_side / (2 * 3**0.5)  # Align the base with the circle
draw_triangle(drawer, triangle_x, triangle_y, triangle_side)

# Draw the line connecting the base of the circle to the base of the triangle
line_start_x = circle_x
line_start_y = circle_y - circle_radius
line_end_x = triangle_x
line_end_y = triangle_y
draw_line(drawer, line_start_x, line_start_y, line_end_x, line_end_y)

# Hide the turtle and display the result
drawer.hideturtle()
screen.mainloop()