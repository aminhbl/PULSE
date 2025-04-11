import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.color("black")

# Function to draw a line
def draw_line(length):
    t.forward(length)

# Function to draw a circle
def draw_circle(radius):
    t.circle(radius)

# Move to the starting point
t.penup()
t.goto(0, 0)
t.pendown()

# Draw the star-like pattern
num_lines = 6
angle = 360 / num_lines
line_length = 100
circle_radius = 10

for _ in range(num_lines):
    draw_line(line_length)
    draw_circle(circle_radius)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.right(angle)

# Hide the turtle and display the result
t.hideturtle()
screen.mainloop()