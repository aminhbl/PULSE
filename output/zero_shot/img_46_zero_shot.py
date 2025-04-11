import turtle

def draw_pentagon(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(72)

def draw_overlapping_pentagons(t, size, count):
    for _ in range(count):
        draw_pentagon(t, size)
        t.forward(size)

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.penup()
t.goto(-200, 0)  # Start position
t.pendown()

# Draw 5 overlapping pentagons
draw_overlapping_pentagons(t, 100, 5)

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()