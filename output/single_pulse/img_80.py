import turtle

def draw_octagon(t, length):
    for _ in range(8):
        t.forward(length)
        t.left(45)

def draw_pattern():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.color("black")
    t.speed(0)  # Fastest drawing speed

    length = 100  # Length of each side of the octagon
    num_octagons = 8
    rotation_angle = 360 / num_octagons

    for _ in range(num_octagons):
        draw_octagon(t, length)
        t.left(rotation_angle)

    t.hideturtle()
    screen.mainloop()

draw_pattern()