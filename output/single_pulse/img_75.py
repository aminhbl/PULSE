import turtle

# Function to draw a circle
def draw_circle(t, radius):
    t.penup()
    t.forward(radius)
    t.left(90)
    t.pendown()
    t.circle(radius)
    t.penup()
    t.right(90)
    t.backward(radius)
    t.pendown()

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
t = turtle.Turtle()
t.color("black")
t.speed(1)

# Define the radius of the circles
radius = 50

# Draw the bottom circle
draw_circle(t, radius)

# Move to the position for the top-left circle
t.penup()
t.goto(-radius, radius * 1.732)  # 1.732 is approximately sqrt(3)
t.pendown()

# Draw the top-left circle
draw_circle(t, radius)

# Move to the position for the top-right circle
t.penup()
t.goto(radius, radius * 1.732)
t.pendown()

# Draw the top-right circle
draw_circle(t, radius)

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()