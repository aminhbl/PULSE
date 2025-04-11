import turtle

def draw_hexagon(t, size):
    for _ in range(6):
        t.forward(size)
        t.left(60)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.color("black")
    t.speed(0)
    
    size = 100  # Size of each hexagon side
    
    # Draw the first hexagon
    draw_hexagon(t, size)
    
    # Move to the position for the second hexagon
    t.penup()
    t.forward(size)
    t.pendown()
    
    # Draw the second hexagon
    draw_hexagon(t, size)
    
    # Move to the position for the third hexagon
    t.penup()
    t.backward(size)
    t.left(60)
    t.forward(size)
    t.right(60)
    t.pendown()
    
    # Draw the third hexagon
    draw_hexagon(t, size)
    
    # Hide the turtle and display the window
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()