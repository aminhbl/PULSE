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
    t.speed(0)  # Fastest drawing speed

    # Initial size of the smallest square
    size = 20
    # Increment size for each subsequent square
    increment = 20

    # Draw six squares
    for _ in range(6):
        draw_square(t, size)
        size += 20  # Increase size for the next square
        y -= 20    # Move the starting point down for the next square

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()