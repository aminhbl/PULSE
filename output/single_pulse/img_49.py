import turtle

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.color("black")
t.speed(1)

# Size of each square
square_size = 100

# Draw the first square
draw_square(t, square_size)

# Move to the position for the second square
t.penup()
t.forward(square_size)
t.pendown()

# Draw the second square
draw_square(t, square_size)

# Move to the position for the third square
t.penup()
t.forward(square_size)
t.pendown()

# Draw the third square
draw_square(t, square_size)

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()