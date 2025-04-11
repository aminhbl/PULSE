import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
starburst = turtle.Turtle()
starburst.speed(0)  # Fastest speed

# Function to draw a pentagon
def draw_pentagon(size):
    for _ in range(5):
        starburst.forward(size)
        starburst.right(72)

# Number of lines/pentagons
num_pentagons = 8
angle_between = 360 / num_pentagons
line_length = 100
pentagon_size = 50

# Draw the starburst pattern
for _ in range(num_pentagons):
    starburst.penup()
    starburst.goto(0, 0)
    starburst.pendown()
    starburst.forward(line_length)
    draw_pentagon(pentagon_size)
    starburst.right(angle_between)

# Hide the turtle and display the window
starburst.hideturtle()
screen.mainloop()