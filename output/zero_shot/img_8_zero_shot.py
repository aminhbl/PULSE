import turtle

def draw_nested_circles():
    screen = turtle.Screen()
    screen.bgcolor("white")

    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()

    # Starting position
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()

    # Number of circles
    num_circles = 6
    # Initial radius
    initial_radius = 20
    # Radius increment
    radius_increment = 20

    for i in range(num_circles):
        # Calculate the current radius
        current_radius = initial_radius + i * radius_increment
        # Calculate the center y position for the current circle
        center_y = -current_radius

        # Move to the starting point of the circle
        pen.penup()
        pen.goto(0, center_y)
        pen.pendown()

        # Draw the circle
        pen.circle(current_radius)

    screen.mainloop()

draw_nested_circles()