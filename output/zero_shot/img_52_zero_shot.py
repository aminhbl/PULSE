import turtle

def draw_pentagon(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(72)

def draw_connected_pentagons():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, 0)
    t.pendown()

    # Draw the first pentagon
    draw_pentagon(t, 100)

    # Move to the next position for the second pentagon
    t.penup()
    t.goto(0, 0)
    t.setheading(72)
    t.pendown()

    # Draw the second pentagon
    draw_pentagon(t, 100)

    # Move to the next position for the third pentagon
    t.penup()
    t.goto(0, 0)
    t.setheading(-72)
    t.pendown()

    # Draw the third pentagon
    draw_pentagon(t, 100)

    t.hideturtle()
    screen.mainloop()

draw_connected_pentagons()