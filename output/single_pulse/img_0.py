import turtle

def draw_square_spiral():
    # Setup the screen
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    # Setup the turtle
    spiral_turtle = turtle.Turtle()
    spiral_turtle.color("black")
    spiral_turtle.speed(0)  # Fastest speed
    spiral_turtle.penup()
    spiral_turtle.goto(0, 0)
    spiral_turtle.pendown()
    
    # Draw the square spiral
    step = 10
    for i in range(1, 21):  # Adjust the range for more or fewer turns
        spiral_turtle.forward(step * i)
        spiral_turtle.right(90)
    
    # Draw the vertical line from the top-left corner
    spiral_turtle.penup()
    spiral_turtle.goto(-step * 10, step * 10)
    spiral_turtle.setheading(270)  # Point downwards
    spiral_turtle.pendown()
    spiral_turtle.forward(step * 20)
    
    # Hide the turtle and finish
    spiral_turtle.hideturtle()
    screen.mainloop()

draw_square_spiral()