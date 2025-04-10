import turtle

def draw_octagon(side_length):
    for _ in range(8):
        turtle.forward(side_length)
        turtle.left(45)

def main():
    # Setup the screen
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Setup the turtle
    turtle.speed(1)
    turtle.color("black")
    turtle.pensize(2)

    # Draw the octagon
    draw_octagon(100)

    # Hide the turtle and finish
    turtle.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()