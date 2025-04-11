import turtle

# Function to draw a heptagon
def draw_heptagon(t, size):
    for _ in range(7):
        t.forward(size)
        t.left(360 / 7)

# Function to draw a pentagon
def draw_pentagon(t, size):
    for _ in range(5):
        t.forward(size)
        t.left(360 / 5)

# Function to draw a line
def draw_line(t, length):
    t.forward(length)

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
t = turtle.Turtle()
t.color("black")
t.pensize(2)
t.speed(1)

# Draw the heptagon on the left side
t.penup()
t.goto(-150, 0)
t.pendown()
draw_heptagon(t, 50)

# Draw the pentagon on the right side
t.penup()
t.goto(50, 0)
t.pendown()
draw_pentagon(t, 50)

# Connect the base of the heptagon to the base of the pentagon
t.penup()
t.goto(-150, 0)
t.pendown()
draw_line(t, 200)

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()