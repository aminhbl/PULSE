import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("white")

# Function to draw a circle with a bold black outline
def draw_circle(x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.pensize(3)
    t.pencolor("black")
    t.fillcolor("")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Parameters
radius = 50
overlap = 20  # Amount by which circles overlap

# Draw five interlocking circles
for i in range(5):
    draw_circle(i * (2 * radius - overlap), 0, radius)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()