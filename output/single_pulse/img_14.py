import turtle

def draw_zigzag(t, steps, step_length, step_height):
    for _ in range(steps):
        t.right(45)
        t.forward(step_length)
        t.left(90)
        t.forward(step_height)
        t.right(45)

def main():
    # Setup the screen
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Create a turtle
    zigzag_turtle = turtle.Turtle()
    zigzag_turtle.color("black")
    zigzag_turtle.speed(1)  # Slow down the drawing for better visualization

    # Initial position
    zigzag_turtle.penup()
    zigzag_turtle.goto(-100, 100)
    zigzag_turtle.pendown()

    # Draw the zigzag pattern
    draw_zigzag(zigzag_turtle, steps=4, step_length=50, step_height=50)

    # Hide the turtle and finish
    zigzag_turtle.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()