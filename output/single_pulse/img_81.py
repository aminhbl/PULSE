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

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
t = turtle.Turtle()
t.color("black")
t.speed(1)

# Define the radius of the circles
radius = 50

# Draw the bottom circle
t.penup()
t.goto(0, -radius)
t.pendown()
draw_circle(t, radius)

# Calculate the distance between the centers of the circles
distance = radius * 2 * 1.5  # Adjust the multiplier for spacing

# Draw the top-left circle
t.penup()
t.goto(-distance / 2, distance * 0.866 - radius)  # 0.866 is sin(60 degrees)
t.pendown()
draw_circle(t, radius)

# Draw the top-right circle
t.penup()
t.goto(distance / 2, distance * 0.866 - radius)
t.pendown()
draw_circle(t, radius)

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()