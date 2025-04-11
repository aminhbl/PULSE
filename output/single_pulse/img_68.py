import turtle

def draw_line(t, length):
    t.forward(length)

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_image():
    # Set up the turtle
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.color("black")
    t.speed(0)
    
    # Define parameters
    line_length = 100
    square_size = 50
    
    # Draw the first line and square
    t.penup()
    t.goto(0, 0)
    t.pendown()
    draw_line(t, line_length)
    t.penup()
    t.goto(line_length - square_size / 2, -square_size / 2)
    t.pendown()
    draw_square(t, square_size)
    
    # Draw the second line and square
    t.penup()
    t.goto(0, 0)
    t.setheading(120)
    t.pendown()
    draw_line(t, line_length)
    t.penup()
    t.goto(line_length * 0.5 - square_size / 2, line_length * (3**0.5) / 2 - square_size / 2)
    t.pendown()
    draw_square(t, square_size)
    
    # Draw the third line and square
    t.penup()
    t.goto(0, 0)
    t.setheading(240)
    t.pendown()
    draw_line(t, line_length)
    t.penup()
    t.goto(-line_length * 0.5 - square_size / 2, line_length * (3**0.5) / 2 - square_size / 2)
    t.pendown()
    draw_square(t, square_size)
    
    # Hide the turtle and display the result
    t.hideturtle()
    screen.mainloop()

draw_image()