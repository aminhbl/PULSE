import turtle

def draw_octagon(side_length):
    for _ in range(8):
        turtle.forward(side_length)
        turtle.left(45)

def draw_semi_circle(radius, direction):
    # Determine the heading based on the direction
    if direction == "up":
        turtle.setheading(0)
    elif direction == "down":
        turtle.setheading(180)
    elif direction == "left":
        turtle.setheading(90)
    elif direction == "right":
        turtle.setheading(270)
    else:
        print("Invalid direction. Use 'up', 'down', 'left', or 'right'.")
        return
    
    # Draw the semi-circle
    turtle.circle(radius, 180)

def main():
    # Setup the screen
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Setup the turtle
    turtle.speed(1)
    turtle.color("black")
    turtle.pensize(2)

    # Draw the octagon on the left side
    turtle.penup()
    turtle.goto(-150, 0)
    turtle.pendown()
    draw_octagon(100)

    # Draw the semi-circle on the right side
    turtle.penup()
    turtle.goto(150, 0)
    turtle.pendown()
    draw_semi_circle(100, "left")

    # Hide the turtle and finish
    turtle.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()