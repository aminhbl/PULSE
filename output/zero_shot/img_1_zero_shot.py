import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.speed(0)
t.color("black")
t.width(2)

# Function to draw a random line
def draw_random_line():
    angle = random.randint(0, 360)
    length = random.randint(50, 150)
    t.setheading(angle)
    t.forward(length)
    t.backward(length)

# Draw the abstract geometric figure
t.penup()
t.goto(0, 0)
t.pendown()

# Draw multiple lines to create the abstract shape
for _ in range(100):
    draw_random_line()

# Hide the turtle and finish
t.hideturtle()
turtle.done()