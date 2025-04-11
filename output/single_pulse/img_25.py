import turtle

def draw_semi_circle(t, radius, direction):
    t.begin_fill()
    t.circle(radius, 180)
    t.end_fill()
    if direction == "left":
        t.right(180)
    else:
        t.left(180)

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
t = turtle.Turtle()
t.color("black")
t.pensize(3)
t.speed(1)

# Draw the smaller semi-circle on the left
t.penup()
t.goto(-150, 50)  # Position the turtle for the smaller semi-circle
t.pendown()
draw_semi_circle(t, 50, "right")

# Draw the larger semi-circle on the right
t.penup()
t.goto(50, 0)  # Position the turtle for the larger semi-circle
t.pendown()
draw_semi_circle(t, 100, "left")

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()