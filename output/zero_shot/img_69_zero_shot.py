import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
star_turtle = turtle.Turtle()
star_turtle.speed(0)  # Fastest speed
star_turtle.penup()

# Function to draw a line with a circle at the end
def draw_line_with_circle(length, circle_radius):
    star_turtle.pendown()
    star_turtle.forward(length)
    star_turtle.circle(circle_radius)
    star_turtle.penup()
    star_turtle.backward(length)

# Main drawing function
def draw_star_with_circles():
    num_lines = 6
    angle_between_lines = 360 / num_lines
    line_length = 100
    circle_radius = 10

    for _ in range(num_lines):
        draw_line_with_circle(line_length, circle_radius)
        star_turtle.right(angle_between_lines)

# Move the turtle to the starting position
star_turtle.goto(0, 0)

# Draw the star with circles
draw_star_with_circles()

# Hide the turtle and display the result
star_turtle.hideturtle()
screen.mainloop()