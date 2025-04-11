import turtle

def draw_snowflake_arm(t, length, circle_radius):
    # Draw a short space
    t.penup()
    t.forward(length)
    t.pendown()
    
    # Draw a short line
    t.forward(length)
    
    # Draw another short space
    t.penup()
    t.forward(length)
    t.pendown()
    
    # Draw a small circle
    t.penup()
    t.forward(circle_radius)
    t.pendown()
    t.circle(circle_radius)
    t.penup()
    t.backward(circle_radius * 2 + length * 2)
    t.pendown()

def draw_snowflake(t, arms, length, circle_radius):
    angle = 360 / arms
    for _ in range(arms):
        draw_snowflake_arm(t, length, circle_radius)
        t.right(angle)

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.color("blue")

# Parameters for the snowflake
arms = 3
length = 20
circle_radius = 10

# Draw the snowflake
draw_snowflake(t, arms, length, circle_radius)

# Hide the turtle and display the result
t.hideturtle()
screen.mainloop()