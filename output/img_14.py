import turtle

def draw_zigzag(steps, step_length, step_height):
    for _ in range(steps):
        turtle.forward(step_length)
        turtle.right(135)
        turtle.forward(step_height)
        turtle.left(135)

def main():
    # Setup the screen
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    # Setup the turtle
    turtle.speed(1)
    turtle.color("black")
    turtle.penup()
    turtle.goto(-100, 100)  # Starting position
    turtle.pendown()
    
    # Draw the zigzag pattern
    draw_zigzag(4, 50, 50)
    
    # Hide the turtle and finish
    turtle.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()