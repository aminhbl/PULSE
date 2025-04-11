import turtle

# Function to draw a line
def draw_line(t, length):
    t.forward(length)

# Function to draw a pentagon
def draw_pentagon(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(72)

# Setup the turtle
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.color("black")
t.speed(0)  # Fastest speed
t.penup()

# Central point
center_x, center_y = 0, 0
t.goto(center_x, center_y)

# Parameters
line_length = 100
pentagon_size = 30
num_lines = 8
angle_between_lines = 360 / num_lines

# Draw the starburst pattern
for _ in range(num_lines):
    t.setheading(angle_between_lines * _)
    t.pendown()
    draw_line(t, line_length)
    t.penup()
    t.forward(pentagon_size / 2)  # Move to the start of the pentagon
    t.pendown()
    draw_pentagon(t, pentagon_size)
    t.penup()
    t.goto(center_x, center_y)

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()