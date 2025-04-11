import turtle

def draw_spiral():
    # Setup the turtle
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.pencolor("black")
    turtle.penup()
    
    # Start at the center of the canvas
    turtle.goto(0, 0)
    turtle.pendown()
    
    # Initial square size
    size = 20
    
    # Draw the initial small square
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    
    # Move to the bottom-right corner of the initial square
    turtle.penup()
    turtle.goto(size, -size)
    turtle.pendown()
    
    # Draw the spiral
    while True:
        # Extend the line to the right
        size += 20
        turtle.forward(size)
        
        # Extend the line upward
        size += 20
        turtle.left(90)
        turtle.forward(size)
        
        # Extend the line to the left
        size += 20
        turtle.left(90)
        turtle.forward(size)
        
        # Extend the line downward
        size += 20
        turtle.left(90)
        turtle.forward(size)
        
        # Check if the spiral has reached the top-left corner
        if turtle.xcor() <= -turtle.window_width() // 2 or turtle.ycor() >= turtle.window_height() // 2:
            break
    
    # Draw the final vertical line downward
    turtle.left(90)
    turtle.forward(turtle.window_height())
    
    # Hide the turtle and finish
    turtle.hideturtle()
    turtle.done()

# Run the program
draw_spiral()