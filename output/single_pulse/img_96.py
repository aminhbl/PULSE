import turtle

def draw_line(t, length):
    t.penup()
    t.forward(20)  # Leave a small gap from the center
    t.pendown()
    t.forward(length)
    t.penup()
    t.backward(length + 20)  # Return to the original position

def draw_triangle(t, side_length):
    t.pendown()
    for _ in range(3):
        t.forward(side_length)
        t.left(120)
    t.penup()

def draw_snowflake_arm(t, line_length, triangle_side):
    draw_line(t, line_length)
    t.forward(line_length)
    draw_triangle(t, triangle_side)
    t.backward(line_length)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.color("black")
    t.speed(0)  # Fastest drawing speed

    line_length = 100
    triangle_side = 30

    for _ in range(3):
        draw_snowflake_arm(t, line_length, triangle_side)
        t.left(120)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()