import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.speed(0)

# Function to draw a triangle
def draw_triangle(vertices, color):
    t.penup()
    t.goto(vertices[0])
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for vertex in vertices[1:]:
        t.goto(vertex)
    t.goto(vertices[0])
    t.end_fill()

# Common center vertex
center = (0, 0)

# Define the vertices for the three triangles
triangle1 = [center, (-100, -173), (100, -173)]  # Downward pointing triangle
triangle2 = [center, (-100, 173), (-200, 0)]     # Left upward pointing triangle
triangle3 = [center, (100, 173), (200, 0)]       # Right upward pointing triangle

# Draw the triangles
draw_triangle(triangle1, "red")
draw_triangle(triangle2, "green")
draw_triangle(triangle3, "blue")

# Hide the turtle
t.hideturtle()

# Keep the window open
screen.mainloop()