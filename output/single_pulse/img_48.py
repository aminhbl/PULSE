import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("white")

# Function to draw a circle with a black outline and white fill
def draw_circle(radius):
    t.fillcolor("white")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Move to the starting position for the first circle
t.penup()
t.goto(-150, 0)
t.pendown()

# Draw the first circle
draw_circle(50)

# Move to the starting position for the second circle
t.penup()
t.goto(-50, 0)
t.pendown()

# Draw the second circle
draw_circle(50)

# Move to the starting position for the third circle
t.penup()
t.goto(50, 0)
t.pendown()

# Draw the third circle
draw_circle(50)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()