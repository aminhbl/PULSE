import turtle

def draw_curved_line(t, length, angle, curve_angle, curve_length):
    t.forward(length)
    t.left(curve_angle)
    t.circle(curve_length, angle)

def draw_flower(t, num_lines, line_length, curve_angle, curve_length):
    for _ in range(num_lines):
        draw_curved_line(t, line_length, 60, curve_angle, curve_length)
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.right(360 / num_lines)

def main():
    # Setup the screen
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Create a turtle
    t = turtle.Turtle()
    t.color("black")
    t.speed(0)  # Fastest speed
    t.penup()
    t.goto(0, 0)
    t.pendown()

    # Draw the flower-like shape
    draw_flower(t, num_lines=6, line_length=100, curve_angle=60, curve_length=50)

    # Hide the turtle and finish
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()