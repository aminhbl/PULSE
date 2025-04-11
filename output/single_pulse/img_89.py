import turtle

def draw_line(t, length):
    t.penup()
    t.forward(length)
    t.pendown()
    t.forward(50)  # Draw the line
    t.penup()
    t.forward(20)  # Leave a small gap before the pentagon
    t.pendown()

def draw_pentagon(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(72)

def draw_arm(t, length, pentagon_size):
    draw_line(t, length)
    draw_pentagon(t, pentagon_size)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.color("black")
    t.speed(0)

    # Move to the starting point without drawing
    t.penup()
    t.goto(0, -20)  # Start slightly below the center
    t.pendown()

    # Draw three arms of the snowflake
    for _ in range(3):
        draw_arm(t, 50, 30)  # Adjust length and pentagon size as needed
        t.penup()
        t.goto(0, -20)  # Return to the starting point
        t.pendown()
        t.right(120)  # Rotate 120 degrees for the next arm

    t.hideturtle()
    screen.mainloop()

main()