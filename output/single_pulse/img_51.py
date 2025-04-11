import turtle

def draw_octagon(t, size):
    for _ in range(8):
        t.forward(size)
        t.left(45)

def draw_flower_of_octagons():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.color("black")
    t.speed(0)  # Fastest drawing speed

    # Center the first octagon
    t.penup()
    t.goto(0, -50)
    t.pendown()

    # Draw the first octagon
    draw_octagon(t, 100)

    # Draw the remaining octagons in a circular pattern
    for angle in range(45, 360, 72):  # 72 degrees between each octagon
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        t.forward(50)
        t.pendown()
        draw_octagon(t, 100)

    t.hideturtle()
    screen.mainloop()

draw_flower_of_octagons()