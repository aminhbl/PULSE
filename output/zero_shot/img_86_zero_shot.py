import turtle

def draw_heptagon(t, size):
    for _ in range(7):
        t.forward(size)
        t.left(360 / 7)

def position_turtle(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def main():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    
    t = turtle.Turtle()
    t.speed(0)
    
    size = 100
    spacing = 1.5 * size
    
    # Draw bottom heptagon
    position_turtle(t, 0, -spacing)
    draw_heptagon(t, size)
    
    # Draw top-left heptagon
    position_turtle(t, -spacing / 2, spacing / 2)
    draw_heptagon(t, size)
    
    # Draw top-right heptagon
    position_turtle(t, spacing / 2, spacing / 2)
    draw_heptagon(t, size)
    
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()