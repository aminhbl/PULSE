import turtle

def draw_line(t, length):
    t.forward(length)

def draw_heptagon(t, side_length):
    for _ in range(7):
        t.forward(side_length)
        t.right(360 / 7)

def main():
    # Set up the turtle
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.color("black")
    t.speed(0)
    
    # Central point
    t.penup()
    t.goto(0, 0)
    t.pendown()
    
    # Parameters
    line_length = 100
    heptagon_side_length = 50
    
    # Draw first line and heptagon
    draw_line(t, line_length)
    draw_heptagon(t, heptagon_side_length)
    
    # Return to central point
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()
    
    # Draw second line and heptagon
    t.left(120)
    draw_line(t, line_length)
    draw_heptagon(t, heptagon_side_length)
    
    # Return to central point
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()
    
    # Draw third line and heptagon
    t.left(240)
    draw_line(t, line_length)
    draw_heptagon(t, heptagon_side_length)
    
    # Hide the turtle and display the window
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()