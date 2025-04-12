import turtle

def draw_heptagon(t, size):
    for _ in range(7):
        t.forward(size)
        t.left(360 / 7)

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    
    t = turtle.Turtle()
    t.speed(0)
    
    # Calculate positions for the heptagons
    distance = 200  # Distance between the centers of the heptagons
    size = 70  # Size of each heptagon
    
    # Position for the bottom heptagon
    bottom_x = 0
    bottom_y = -distance / (2 * (3**0.5))
    
    # Positions for the top heptagons
    top_left_x = -distance / 2
    top_left_y = distance / (2 * (3**0.5))
    
    top_right_x = distance / 2
    top_right_y = distance / (2 * (3**0.5))
    
    # Draw bottom heptagon
    t.penup()
    t.goto(bottom_x, bottom_y)
    t.pendown()
    draw_heptagon(t, size)
    
    # Draw top left heptagon
    t.penup()
    t.goto(top_left_x, top_left_y)
    t.pendown()
    draw_heptagon(t, size)
    
    # Draw top right heptagon
    t.penup()
    t.goto(top_right_x, top_right_y)
    t.pendown()
    draw_heptagon(t, size)
    
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()