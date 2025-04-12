import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
star_turtle = turtle.Turtle()
star_turtle.speed(0)  # Fastest speed
star_turtle.penup()

# Function to draw a line with a circle at the end
def draw_line_with_circle(length, angle):
    star_turtle.setheading(angle)
    star_turtle.pendown()
    star_turtle.forward(length)
    star_turtle.penup()
    star_turtle.forward(10)  # Move a bit further to draw the circle
    star_turtle.pendown()
    star_turtle.circle(10)  # Draw a circle with radius 10
    star_turtle.penup()
    star_turtle.backward(length + 10)  # Return to the center

# Draw the star-like pattern
num_lines = 7
angle_between_lines = 360 / num_lines
line_length = 100

for i in range(num_lines):
    draw_line_with_circle(line_length, i * angle_between_lines)

# Hide the turtle and display the window
star_turtle.hideturtle()
screen.mainloop()