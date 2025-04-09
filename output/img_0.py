import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
my_turtle = turtle.Turtle()
my_turtle.pensize(3)            # Set the border thickness
my_turtle.color("black")        # Use black color for the border
my_turtle.speed(1)

# Function to draw a hexagon
def draw_hexagon(t, side_length):
    for _ in range(6):
        t.forward(side_length)
        t.left(60)

# Function to draw a circle
def draw_circle(t, radius):
    t.circle(radius)

# Draw a small hexagon on the left
my_turtle.penup()
my_turtle.goto(-150, 0)  # Position for the hexagon
my_turtle.pendown()

# Draw the small hexagon
draw_hexagon(my_turtle, 30)  # Small hexagon with side length 30

# Draw a small circle on the right
my_turtle.penup()
my_turtle.goto(150, -30)  # Position for the circle, adjusted for radius
my_turtle.pendown()

# Draw the small circle
draw_circle(my_turtle, 30)  # Small circle with radius 30

# Hide the turtle
my_turtle.hideturtle()

# Wait for user click to close the window
screen.exitonclick()
