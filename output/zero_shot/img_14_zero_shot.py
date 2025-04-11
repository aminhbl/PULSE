import turtle

def draw_ladder():
    # Set up the turtle
    t = turtle.Turtle()
    t.speed(1)
    
    # Define the step size
    step_length = 100
    step_height = 50
    
    # Draw the ladder
    for _ in range(4):
        # Draw the right slanting step
        t.left(45)
        t.forward(step_length)
        
        # Draw the vertical part of the step
        t.right(90)
        t.forward(step_height)
        
        # Draw the left slanting step
        t.right(135)
        t.forward(step_length)
        
        # Draw the vertical part of the step
        t.left(90)
        t.forward(step_height)
    
    # Hide the turtle and display the window
    t.hideturtle()
    turtle.done()

draw_ladder()