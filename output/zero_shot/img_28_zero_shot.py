import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Pentagon and Circle with Turtle")
screen.bgcolor("white")

# Set up the turtle
t = turtle.Turtle()
t.pensize(3)  # Bold black lines
t.speed(1)

# Draw a pentagon
t.penup()
t.goto(-150, 0)  # Start position for the pentagon
t.pendown()
t.color("black")
t.begin_fill()
for _ in range(5):
    t.forward(100)
    t.right(72)
t.end_fill()

# Draw a line connecting the pentagon and circle
t.penup()
t.goto(-50, 0)
t.pendown()
t.forward(200)

# Draw a circle
t.penup()
t.goto(150, -50)  # Start position for the circle
t.pendown()
t.circle(50)

# Hide the turtle and finish
t.hideturtle()
screen.mainloop()