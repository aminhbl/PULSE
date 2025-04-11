import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Three Adjacent Squares")

# Create a turtle
t = turtle.Turtle()
t.speed(1)

# Function to draw a square
def draw_square(side_length):
    for _ in range(4):
        t.forward(side_length)
        t.right(90)

# Set the side length of the squares
side_length = 100

# Draw three adjacent squares
for _ in range(3):
    draw_square(side_length)
    t.forward(side_length)

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()