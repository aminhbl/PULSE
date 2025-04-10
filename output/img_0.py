import turtle

def draw_square_spiral():
    # Setup the turtle
    turtle.setup(width=600, height=600)
    turtle.bgcolor("white")
    turtle.speed(0)
    turtle.pensize(2)
    turtle.color("black")
    
    # Start drawing from the center
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    
    # Draw the initial small square
    side_length = 20
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)
    
    # Draw the spiral
    step_increase = 10
    for _ in range(20):  # Adjust the range for desired spiral size
        side_length += step_increase
        turtle.forward(side_length)
        turtle.right(90)
    
    # Draw the final vertical line from the top-left corner
    turtle.penup()
    turtle.goto(-side_length/2, side_length/2)
    turtle.pendown()
    turtle.setheading(270)  # Point downwards
    turtle.forward(600)  # Extend to the bottom of the canvas
    
    # Hide the turtle and finish
    turtle.hideturtle()
    turtle.done()

draw_square_spiral()