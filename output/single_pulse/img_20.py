import turtle

def draw_nonagon(t, side_length):
    t.pendown()
    t.pensize(3)
    t.pencolor("black")
    for _ in range(9):
        t.forward(side_length)
        t.left(40)
    t.penup()

def draw_semi_circle(t, radius):
    t.pendown()
    t.pensize(3)
    t.pencolor("black")
    t.setheading(90)  # Start from the top of the semi-circle
    t.circle(radius, 180)  # Draw a semi-circle
    t.penup()

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    # Draw nonagon
    nonagon_side_length = 100
    t.goto(-150, 0)  # Position turtle for nonagon
    draw_nonagon(t, nonagon_side_length)

    # Draw semi-circle
    semi_circle_radius = 50
    t.goto(100, 50)  # Position turtle for semi-circle
    draw_semi_circle(t, semi_circle_radius)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()