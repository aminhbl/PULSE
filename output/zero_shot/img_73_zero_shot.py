import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
pen = turtle.Turtle()
pen.speed(0)  # Fastest speed
pen.color("black")

# Function to draw a triangle
def draw_triangle():
    for _ in range(3):
        pen.forward(20)
        pen.left(120)

# Draw eight lines with triangles at the end
for _ in range(8):
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.forward(100)
    draw_triangle()
    pen.penup()
    pen.goto(0, 0)
    pen.left(45)

# Hide the turtle and display the window
pen.hideturtle()
screen.mainloop()