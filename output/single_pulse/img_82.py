import turtle

def draw_arc(t, radius, extent):
    t.circle(radius, extent)

def draw_flower():
    # Setup the screen
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Setup the turtle
    t = turtle.Turtle()
    t.color("black")
    t.speed(0)  # Fastest drawing speed
    t.width(2)  # Set the width of the pen

    # Draw the flower-like pattern
    num_arcs = 8
    arc_radius = 100
    arc_extent = 60
    angle_between_arcs = 360 / num_arcs

    for _ in range(num_arcs):
        draw_arc(t, arc_radius, arc_extent)
        t.left(angle_between_arcs)

    # Hide the turtle and finish
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    draw_flower()