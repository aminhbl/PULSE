import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Heptagon and Pentagon")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.speed(1)

# Function to draw a polygon
def draw_polygon(t, sides, length):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.right(angle)

# Draw a heptagon on the left
drawer.penup()
drawer.goto(-150, 0)
drawer.pendown()
draw_polygon(drawer, 7, 50)

# Draw a pentagon on the right
drawer.penup()
drawer.goto(50, 0)
drawer.pendown()
draw_polygon(drawer, 5, 50)

# Draw a horizontal line connecting the bases
drawer.penup()
drawer.goto(-150, 0)
drawer.pendown()
drawer.goto(50, 0)

# Hide the turtle
drawer.hideturtle()

# Finish
screen.mainloop()