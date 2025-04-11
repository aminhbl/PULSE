import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
t = turtle.Turtle()
t.speed(0)
t.pensize(3)
t.color("black")

# Function to draw a circle
def draw_circle(radius):
    t.penup()
    t.goto(-150, 0)  # Position for the small circle
    t.pendown()
    t.circle(radius)

# Function to draw a semi-circle
def draw_semi_circle(radius):
    t.penup()
    t.goto(50, 0)  # Position for the semi-circle
    t.setheading(90)  # Face upwards
    t.pendown()
    t.circle(radius, 180)  # Draw a semi-circle

# Function to draw a line
def draw_line(length):
    t.penup()
    t.goto(-150, 0)  # Start at the base of the small circle
    t.setheading(0)  # Face right
    t.pendown()
    t.forward(length)

# Draw the small circle
draw_circle(30)

# Draw the semi-circle
draw_semi_circle(60)

# Draw the connecting line
draw_line(200)

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()