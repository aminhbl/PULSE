import turtle

# Function to draw a line
def draw_line(t, length):
    t.forward(length)

# Function to draw an equilateral triangle
def draw_triangle(t, side_length):
    for _ in range(3):
        t.forward(side_length)
        t.left(120)

# Setup the turtle
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.color("black")
t.speed(0)  # Fastest speed
t.penup()

# Central point
central_x, central_y = 0, 0
t.goto(central_x, central_y)

# Parameters
line_length = 100
triangle_side_length = 50
angle_between_lines = 45

# Draw the pattern
for _ in range(8):
    t.setheading(angle_between_lines * _)
    t.pendown()
    draw_line(t, line_length)
    draw_triangle(t, triangle_side_length)
    t.penup()
    t.goto(central_x, central_y)

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()