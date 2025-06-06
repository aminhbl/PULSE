import turtle

def draw_spiral_squares():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    
    side_length = 20  # Initial side length
    increment = 20    # Increment for each subsequent square
    
    for _ in range(6):
        for _ in range(4):
            turtle.forward(side_length)
            turtle.left(90)
        side_length += increment
        turtle.penup()
        turtle.goto(turtle.xcor() - increment / 2, turtle.ycor() - increment / 2)
        turtle.pendown()

    turtle.done()

draw_spiral_squares()