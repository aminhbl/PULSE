import turtle

# Function to draw a regular polygon
def draw_polygon(t, sides, length):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.right(angle)

# Set up the turtle
t = turtle.Turtle()
t.pensize(3)  # Bold lines
t.speed(1)    # Slow speed for drawing

# Draw a regular heptagon
t.penup()
t.goto(-150, 0)  # Position for the heptagon
t.pendown()
draw_polygon(t, 7, 50)

# Draw an equilateral triangle
t.penup()
t.goto(50, 0)  # Position for the triangle
t.pendown()
draw_polygon(t, 3, 50)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()