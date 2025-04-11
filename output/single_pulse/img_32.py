import turtle

# Function to draw a pentagon
def draw_pentagon(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(72)

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
t = turtle.Turtle()
t.color("black")
t.pensize(3)
t.speed(1)

# Calculate positions
canvas_width = screen.window_width()
canvas_height = screen.window_height()
pentagon_size = 100
spacing = 50
total_width = 2 * pentagon_size + spacing

# Position the turtle for the first pentagon
t.penup()
t.goto(-total_width / 2, -pentagon_size / 2)
t.pendown()

# Draw the first pentagon
draw_pentagon(t, pentagon_size)

# Position the turtle for the second pentagon
t.penup()
t.goto(total_width / 2 - pentagon_size, -pentagon_size / 2)
t.pendown()

# Draw the second pentagon
draw_pentagon(t, pentagon_size)

# Draw the connecting line
t.penup()
t.goto(-total_width / 2, -pentagon_size / 2)
t.pendown()
t.forward(total_width - pentagon_size)

# Hide the turtle and finish
t.hideturtle()
screen.mainloop()