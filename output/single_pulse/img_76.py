import turtle

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_pattern():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.color("black")
    t.speed(0)  # Fastest drawing speed

    num_squares = 6
    square_size = 100
    angle_between_squares = 360 / num_squares
    rotation_angle = 15  # Slight rotation for each subsequent square

    for i in range(num_squares):
        draw_square(t, square_size)
        t.penup()
        t.forward(square_size / 2)
        t.right(rotation_angle)
        t.forward(square_size / 2)
        t.pendown()
        t.right(angle_between_squares)

    t.hideturtle()
    screen.mainloop()

draw_pattern()