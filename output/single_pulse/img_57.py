import turtle

def draw_semicircle(t, radius):
    t.circle(radius, 180)

def draw_pinwheel():
    # Set up the turtle
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.color("black")
    t.speed(0)  # Fastest drawing speed

    # Central point
    central_x, central_y = 0, 0
    t.penup()
    t.goto(central_x, central_y)
    t.pendown()

    # Radius of the semicircles
    radius = 100

    # Draw three semicircles
    for _ in range(3):
        draw_semicircle(t, radius)
        t.penup()
        t.goto(central_x, central_y)
        t.pendown()
        t.right(120)

    # Hide the turtle and display the window
    t.hideturtle()
    screen.mainloop()

draw_pinwheel()