import turtle

def draw_spiral_squares():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    
    side_length = 20
    increment = 20
    
    for _ in range(5):
        for _ in range(4):
            turtle.forward(side_length)
            turtle.left(90)
        side_length += increment
        turtle.penup()
        turtle.goto(turtle.xcor() - increment, turtle.ycor() - increment)
        turtle.pendown()

    turtle.done()

draw_spiral_squares()