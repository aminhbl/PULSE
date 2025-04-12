import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed

# Function to draw a triangle
def draw_triangle():
    for _ in range(3):
        t.forward(20)
        t.left(120)

# Draw the pattern
for _ in range(8):
    t.forward(100)  # Draw the line
    draw_triangle()  # Draw the triangle at the end
    t.backward(100)  # Go back to the center
    t.left(45)  # Rotate 45 degrees for the next line

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()