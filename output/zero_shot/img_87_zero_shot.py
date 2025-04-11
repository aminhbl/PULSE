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
    
    # Draw a small circle at the end
    t.circle(circle_radius)
    
    # Move back to the center
    t.penup()
    t.backward(3 * length + circle_radius * 2)
    t.pendown()

def draw_snowflake(t, num_arms, arm_length, circle_radius):
    angle = 360 / num_arms
    for _ in range(num_arms):
        draw_snowflake_arm(t, arm_length, circle_radius)
        t.right(angle)

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")

snowflake_turtle = turtle.Turtle()
snowflake_turtle.speed(0)  # Fastest speed
snowflake_turtle.color("blue")

# Draw the snowflake
draw_snowflake(snowflake_turtle, 5, 20, 5)

# Hide the turtle and display the window
snowflake_turtle.hideturtle()
screen.mainloop()