import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
star_turtle = turtle.Turtle()
star_turtle.speed(0)  # Fastest speed
star_turtle.penup()

# Function to draw a heptagon
def draw_heptagon(t, size):
    t.pendown()
    for _ in range(7):
        t.forward(size)
        t.right(360 / 7)
    t.penup()

# Function to draw the star-like pattern with heptagons
def draw_star_with_heptagons(t, num_lines, line_length, heptagon_size):
    angle_between_lines = 360 / num_lines
    for _ in range(num_lines):
        t.forward(line_length)
        draw_heptagon(t, heptagon_size)
        t.backward(line_length)
        t.right(angle_between_lines)

# Draw the pattern
star_turtle.goto(0, 0)
draw_star_with_heptagons(star_turtle, 6, 100, 50)

# Hide the turtle and display the window
star_turtle.hideturtle()
screen.mainloop()