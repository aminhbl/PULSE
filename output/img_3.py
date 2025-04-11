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
    # Number of squares to draw
    num_squares = 8
    
    for i in range(num_squares):
        draw_square(t, size)
        size += 20  # Increase the size for the next square
    
    t.hideturtle()
    screen.mainloop()

main()