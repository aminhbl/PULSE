import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Circle and Line Drawing")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.pensize(3)  # Bold lines
drawer.speed(1)  # Slow speed for drawing

# Draw a circle on the left
drawer.penup()
drawer.goto(-100, 0)  # Move to the left position
drawer.pendown()
drawer.circle(50)  # Draw a circle with radius 50

# Draw a short horizontal line on the right
drawer.penup()
drawer.goto(50, 0)  # Move to the right position
drawer.pendown()
drawer.forward(100)  # Draw a horizontal line

# Hide the turtle and finish
drawer.hideturtle()
screen.mainloop()