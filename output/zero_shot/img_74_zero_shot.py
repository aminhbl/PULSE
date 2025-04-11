import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
starburst = turtle.Turtle()
starburst.speed(0)  # Fastest drawing speed
starburst.penup()

# Function to draw a triangle
def draw_triangle(size):
    for _ in range(3):
        starburst.forward(size)
        starburst.left(120)

# Number of triangles
num_triangles = 8
angle_between = 360 / num_triangles
triangle_size = 100  # Length of the sides of the triangle
line_length = 150  # Length of the line from center to apex

# Draw the starburst pattern
for _ in range(num_triangles):
    starburst.forward(line_length)
    starburst.pendown()
    draw_triangle(triangle_size)
    starburst.penup()
    starburst.goto(0, 0)
    starburst.left(angle_between)

# Hide the turtle and display the window
starburst.hideturtle()
screen.mainloop()