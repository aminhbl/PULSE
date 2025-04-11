import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=400)

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.speed(1)

# Draw a full circle on the left
drawer.penup()
drawer.goto(-200, 0)  # Move to the left side
drawer.pendown()
drawer.circle(50)  # Draw a full circle with radius 50

# Draw a semicircle on the right
drawer.penup()
drawer.goto(200, 0)  # Move to the right side
drawer.pendown()
drawer.setheading(90)  # Face upwards
drawer.circle(50, 180)  # Draw a semicircle with radius 50

# Hide the turtle and finish
drawer.hideturtle()
screen.mainloop()