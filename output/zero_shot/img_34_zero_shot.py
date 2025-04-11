import turtle

def draw_octagon(t, size):
    for _ in range(8):
        t.forward(size)
        t.left(45)

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    
    # Draw the first octagon
    t.goto(-150, 0)
    t.pendown()
    draw_octagon(t, 50)
    t.penup()
    
    # Draw the connecting line
    t.goto(-100, 0)
    t.pendown()
    t.forward(200)
    t.penup()
    
    # Draw the second octagon
    t.goto(150, 0)
    t.pendown()
    draw_octagon(t, 50)
    t.penup()
    
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()