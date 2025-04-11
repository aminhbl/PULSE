import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Circle and Pentagon with Turtle")
screen.bgcolor("white")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.speed(1)
drawer.pensize(3)  # Bold lines

# Draw the circle on the left
drawer.penup()
drawer.goto(-150, 0)  # Move to the left position
drawer.pendown()
drawer.circle(50)  # Draw a circle with radius 50

# Draw the pentagon on the right
drawer.penup()
drawer.goto(50, 0)  # Move to the right position
drawer.pendown()
drawer.setheading(0)  # Ensure the turtle is facing right

# Draw a pentagon
side_length = 100
for _ in range(5):
    drawer.forward(side_length)
    drawer.right(72)  # 360/5 = 72 degrees

# Draw the connecting line
drawer.penup()
drawer.goto(-100, 0)  # Start from the base of the circle
drawer.pendown()
drawer.goto(50, 0)  # Draw to the base of the pentagon

# Hide the turtle and finish
drawer.hideturtle()
screen.mainloop()