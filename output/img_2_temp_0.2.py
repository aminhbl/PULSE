import turtle

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.left(90)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.color("black")
    t.speed(0)
    
    # Starting size of the smallest square
    size = 20
    # Increment size for each subsequent square
    increment = 20
    
    # Draw 6 squares
    for i in range(6):
        draw_square(t, size)
        size += increment
    
    t.hideturtle()
    screen.mainloop()

main()