import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.speed(0)
drawer.pensize(2)

# Function to draw a full circle
def draw_circle(t, radius):
    t.penup()
    t.goto(-150, 0)  # Position the turtle to the left side of the canvas
    t.pendown()
    t.circle(radius)

# Function to draw a semicircle
def draw_semi_circle(t, radius):
    t.penup()
    t.goto(150, 0)  # Position the turtle to the right side of the canvas
    t.setheading(90)  # Point the turtle upwards
    t.pendown()
    t.circle(radius, 180)  # Draw a semicircle

# Draw a full circle
drawer.color("black")
draw_circle(drawer, 50)

# Draw a semicircle
drawer.color("black")
draw_semi_circle(drawer, 50)

# Hide the turtle and finish
drawer.hideturtle()
screen.mainloop()