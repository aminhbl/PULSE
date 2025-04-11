import turtle

def draw_semi_circle(t, radius):
    t.circle(radius, 180)  # Draw a semi-circle

def draw_pattern():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.color("black")
    t.width(2)

    # Draw central point
    t.penup()
    t.goto(0, 0)
    t.dot(5, "black")

    # Set initial position for the first semi-circle
    t.goto(0, -50)
    t.setheading(90)  # Point upwards

    # Draw 5 semi-circles
    for i in range(5):
        t.pendown()
        draw_semi_circle(t, 50)
        t.penup()
        t.goto(0, 0)  # Return to center
        t.setheading(90 + (i + 1) * 72)  # Rotate for the next semi-circle

    t.hideturtle()
    screen.mainloop()

draw_pattern()