import turtle

def draw_pentagon():
    turtle.penup()
    turtle.goto(-150, 0)  # Position the turtle to the left side of the canvas
    turtle.pendown()
    turtle.pensize(3)
    turtle.pencolor("black")
    for _ in range(5):
        turtle.forward(100)
        turtle.right(72)

def draw_square():
    turtle.penup()
    turtle.goto(50, 0)  # Position the turtle to the right side of the canvas
    turtle.pendown()
    turtle.pensize(3)
    turtle.pencolor("black")
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

# Set up the turtle
turtle.speed(1)
turtle.hideturtle()

# Draw the shapes
draw_pentagon()
draw_square()

# Finish
turtle.done()