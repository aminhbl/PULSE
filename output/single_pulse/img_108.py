import turtle

def draw_circle(radius):
    turtle.penup()
    turtle.goto(0, -radius)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.left(90)

def draw_cluster(radius):
    draw_circle(radius)
    turtle.penup()
    turtle.goto(-radius, 0)
    turtle.pendown()
    draw_square(2 * radius)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

def draw_pattern(radius):
    for angle in [0, 120, 240]:
        turtle.penup()
        turtle.goto(0, 0)
        turtle.setheading(angle)
        turtle.forward(radius * 2)
        turtle.pendown()
        draw_cluster(radius)

# Setup turtle
turtle.speed(0)
turtle.hideturtle()

# Draw the pattern
draw_pattern(50)

# Finish
turtle.done()