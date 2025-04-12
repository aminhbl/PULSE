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
    snowflake.forward(50)  # Draw the arm
    snowflake.penup()
    snowflake.forward(20)  # Move to the position for the circle
    snowflake.pendown()
    snowflake.circle(10)   # Draw a small circle at the end
    snowflake.penup()
    snowflake.backward(120)  # Return to the center

# Draw the five-armed snowflake
for _ in range(5):
    draw_arm()
    snowflake.right(72)  # Turn right to space the arms evenly

# Hide the turtle and display the window
snowflake.hideturtle()
screen.mainloop()