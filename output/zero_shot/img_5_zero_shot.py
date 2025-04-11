import turtle

def draw_spiral_squares():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    
    side_length = 20
    for i in range(7):
        for _ in range(4):
            turtle.forward(side_length)
            turtle.left(90)
        turtle.penup()
        turtle.goto(turtle.xcor() - 10, turtle.ycor() - 10)
        turtle.pendown()
        side_length += 20

    turtle.done()

draw_spiral_squares()