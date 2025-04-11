import turtle

# Function to draw a line
def draw_line(t, length):
    t.penup()
    t.forward(length)
    t.pendown()
    t.forward(50)  # Length of the line
    t.penup()
    t.backward(length + 50)
    t.pendown()

# Function to draw an equilateral triangle
def draw_triangle(t, side_length):
    for _ in range(3):
        t.forward(side_length)
        t.left(120)

# Setup the turtle
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.color("black")
t.speed(0)

# Central point offset
offset = 20

# Draw the snowflake pattern
for _ in range(8):
    t.penup()
    t.forward(offset)
    t.pendown()
    draw_line(t, offset)
    t.penup()
    t.forward(50)  # Move to the end of the line
    t.pendown()
    draw_triangle(t, 30)  # Draw triangle at the end of the line
    t.penup()
    t.backward(50 + offset)  # Return to the center
    t.left(45)  # Rotate to the next arm

t.hideturtle()
screen.mainloop()