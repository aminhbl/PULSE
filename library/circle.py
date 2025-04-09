import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
my_turtle = turtle.Turtle()
my_turtle.pensize(3)            # Set the border thickness
my_turtle.color("black")        # Use black color for the border
my_turtle.speed(1)

# Draw the circle with no fill
radius = 50                     # Radius of the circle

# Move to starting position
my_turtle.penup()
my_turtle.goto(0, -radius)      # Position to draw from bottom of circle
my_turtle.pendown()

# Draw the circle
my_turtle.circle(radius)

# Wait for user click to close the window
screen.exitonclick()
