import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
my_turtle = turtle.Turtle()
my_turtle.pensize(3)            # Set the border thickness
my_turtle.color("black")        # Use black color for the border
my_turtle.speed(1)

# Draw the hexagon with no fill
side_length = 50                # Side length of the hexagon

# Move to starting position
my_turtle.penup()
my_turtle.goto(-side_length/2, -side_length * 0.866)  # Position to center the hexagon
my_turtle.pendown()

# Draw the hexagon
for _ in range(6):
    my_turtle.forward(side_length)
    my_turtle.left(60)

# Wait for user click to close the window
screen.exitonclick()
