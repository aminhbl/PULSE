import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Function to draw a heptagon
def draw_heptagon(t, size):
    t.pensize(3)
    t.color("black")
    t.begin_fill()
    for _ in range(7):
        t.forward(size)
        t.left(360 / 7)
    t.end_fill()

# Function to draw a circle
def draw_circle(t, radius):
    t.pensize(3)
    t.color("black")
    t.circle(radius)

# Create a turtle for drawing
heptagon_turtle = turtle.Turtle()
heptagon_turtle.penup()
heptagon_turtle.goto(-150, 0)  # Position on the left side
heptagon_turtle.pendown()
draw_heptagon(heptagon_turtle, 50)

# Create another turtle for drawing
circle_turtle = turtle.Turtle()
circle_turtle.penup()
circle_turtle.goto(150, -25)  # Position on the right side, slightly lower to align
circle_turtle.pendown()
draw_circle(circle_turtle, 25)

# Hide the turtles
heptagon_turtle.hideturtle()
circle_turtle.hideturtle()

# Finish
turtle.done()