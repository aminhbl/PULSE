import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.speed(0)

# Function to draw a heptagon
def draw_heptagon(size):
    for _ in range(7):
        t.forward(size)
        t.left(360 / 7)

# Function to draw a line with a heptagon at the end
def draw_line_with_heptagon(length, heptagon_size):
    t.forward(length)
    draw_heptagon(heptagon_size)
    t.backward(length)

# Main drawing function
def draw_y_shape_with_heptagons():
    line_length = 100
    heptagon_size = 40

    for _ in range(3):
        draw_line_with_heptagon(line_length, heptagon_size)
        t.left(120)

# Position the turtle
t.penup()
t.goto(0, 0)
t.pendown()

# Draw the Y-shaped structure with heptagons
draw_y_shape_with_heptagons()

# Hide the turtle and display the result
t.hideturtle()
screen.mainloop()