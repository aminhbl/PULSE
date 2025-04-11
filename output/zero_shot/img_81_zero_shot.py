import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Triangle of Circles")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.speed(0)  # Fastest drawing speed

# Function to draw a circle at a specific position
def draw_circle(x, y, radius):
    drawer.penup()
    drawer.goto(x, y - radius)  # Move to the starting point of the circle
    drawer.pendown()
    drawer.circle(radius)
    drawer.penup()

# Parameters
radius = 50
distance = radius * 2  # Distance between the centers of the circles

# Draw the circles
draw_circle(-distance / 2, distance / 2, radius)  # Top left circle
draw_circle(distance / 2, distance / 2, radius)   # Top right circle
draw_circle(0, -distance / 2, radius)             # Bottom center circle

# Hide the turtle and display the window
drawer.hideturtle()
screen.mainloop()