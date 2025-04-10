import turtle

# Function to draw an octagon
def draw_octagon(t, size):
    t.pensize(3)
    t.color("black")
    for _ in range(8):
        t.forward(size)
        t.left(45)

# Function to draw a semi-circle
def draw_semi_circle(t, radius):
    t.pensize(3)
    t.color("black")
    t.setheading(90)  # Start facing upwards
    t.circle(radius, 180)  # Draw a semi-circle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
t = turtle.Turtle()
t.speed(1)

# Draw the octagon on the left side
t.penup()
t.goto(-150, 0)  # Position the turtle to the left
t.pendown()
draw_octagon(t, 50)

# Draw the semi-circle on the right side
t.penup()
t.goto(100, 0)  # Position the turtle to the right
t.pendown()
draw_semi_circle(t, 50)

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()