import turtle

def draw_snowflake_arm():
    # Draw a short space
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
    
    # Draw a short line
    turtle.forward(20)
    
    # Draw another short space
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
    
    # Draw a small semicircle
    turtle.circle(10, 180)

def draw_snowflake():
    for _ in range(8):
        draw_snowflake_arm()
        turtle.penup()
        turtle.home()
        turtle.right(45 * (_ + 1))
        turtle.pendown()

# Set up the turtle
turtle.speed(0)  # Fastest speed
turtle.hideturtle()

# Draw the snowflake
draw_snowflake()

# Finish
turtle.done()