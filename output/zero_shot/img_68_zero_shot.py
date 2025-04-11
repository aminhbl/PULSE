import turtle

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_pinwheel():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)

    # Set the length of the lines and size of the squares
    line_length = 100
    square_size = 20

    # Draw the Y-shaped lines with squares at the end
    for angle in [0, 120, 240]:
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        t.pendown()
        t.forward(line_length)
        
        # Draw the square at the end of the line
        t.right(45)  # Rotate the square for a dynamic appearance
        draw_square(t, square_size)

    t.hideturtle()
    screen.mainloop()

draw_pinwheel()