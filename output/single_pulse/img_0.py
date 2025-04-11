import turtle

def draw_square_spiral(t, length, increment, turns):
    for i in range(turns):
        t.forward(length)
        t.right(90)
        length += increment

def draw_vertical_line(t, length):
    t.penup()
    t.goto(-length/2, length/2)
    t.pendown()
    t.right(90)
    t.forward(length)

def main():
    # Setup the screen
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Create a turtle
    spiral_turtle = turtle.Turtle()
    spiral_turtle.color("black")
    spiral_turtle.speed(0)  # Fastest speed
    spiral_turtle.penup()
    spiral_turtle.goto(0, 0)
    spiral_turtle.pendown()

    # Draw the square spiral
    initial_length = 10
    increment = 10
    turns = 20
    draw_square_spiral(spiral_turtle, initial_length, increment, turns)

    # Draw the vertical line from the top-left corner
    draw_vertical_line(spiral_turtle, initial_length + increment * (turns - 1))

    # Hide the turtle and finish
    spiral_turtle.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()