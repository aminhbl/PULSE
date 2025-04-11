import turtle

def draw_equilateral_triangle(t, side_length):
    for _ in range(3):
        t.forward(side_length)
        t.left(120)

def main():
    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Set up the turtle
    t = turtle.Turtle()
    t.color("black")
    t.pensize(3)
    t.speed(0)

    # Define the side length of the equilateral triangles
    side_length = 100

    # Draw six equilateral triangles in a row
    for _ in range(6):
        draw_equilateral_triangle(t, side_length)
        t.penup()
        t.forward(side_length)
        t.pendown()

    # Hide the turtle and display the window
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()