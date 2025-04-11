import turtle

def draw_circle(t, x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.circle(radius)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(3)
    t.color("black")
    
    radius = 50
    spacing = radius * 1.5  # Adjust spacing to create overlapping effect
    
    # Draw four interlocking circles
    for i in range(4):
        draw_circle(t, i * spacing, 0, radius)
    
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()