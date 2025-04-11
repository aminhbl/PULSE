import turtle

def draw_circle(t, x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.circle(radius)

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=400)
    
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(5)
    t.color("black")
    
    radius = 50
    spacing = radius * 2 - 10  # Overlapping edges
    
    start_x = -2 * spacing
    start_y = 0
    
    for i in range(5):
        draw_circle(t, start_x + i * spacing, start_y, radius)
    
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()