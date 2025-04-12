import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
snowflake = turtle.Turtle()
snowflake.speed(0)  # Fastest drawing speed
snowflake.color("blue")

# Function to draw a single arm of the snowflake
def draw_arm():
    snowflake.penup()
    snowflake.forward(50)  # Move forward to start the arm
    snowflake.pendown()
    snowflake.forward(100)  # Draw the arm
    snowflake.penup()
    snowflake.forward(20)  # Move to the end of the arm
    snowflake.pendown()
    snowflake.circle(10)  # Draw a small circle at the end
    snowflake.penup()
    snowflake.backward(170)  # Return to the center

# Draw the three-armed snowflake
for _ in range(3):
    draw_arm()
    snowflake.right(120)  # Turn to the next arm position

# Hide the turtle and finish
snowflake.hideturtle()
screen.mainloop()