import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
snowflake_turtle = turtle.Turtle()
snowflake_turtle.color("black")
snowflake_turtle.speed(0)  # Fastest drawing speed
snowflake_turtle.penup()

# Function to draw a line
def draw_line(length):
    snowflake_turtle.pendown()
    snowflake_turtle.forward(length)
    snowflake_turtle.penup()

# Function to draw a circle
def draw_circle(radius):
    snowflake_turtle.pendown()
    snowflake_turtle.circle(radius)
    snowflake_turtle.penup()

# Parameters
num_arms = 8
angle_between_arms = 360 / num_arms
line_length = 100
circle_radius = 20
gap_from_center = 10
gap_to_circle = 10

# Draw the snowflake
for _ in range(num_arms):
    # Move to the starting point of the line
    snowflake_turtle.penup()
    snowflake_turtle.goto(0, 0)
    snowflake_turtle.setheading(angle_between_arms * _)
    snowflake_turtle.forward(gap_from_center)
    
    # Draw the line
    draw_line(line_length - gap_from_center - gap_to_circle)
    
    # Move to the starting point of the circle
    snowflake_turtle.forward(gap_to_circle)
    
    # Draw the circle
    draw_circle(circle_radius)

# Hide the turtle and display the result
snowflake_turtle.hideturtle()
screen.mainloop()