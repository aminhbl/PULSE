import turtle

def draw_pentagon(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(72)

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_cluster(t, size, angle):
    draw_pentagon(t, size)
    t.right(angle)
    draw_square(t, size)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    
    size = 100
    angles = [0, 15, 30, 45, 60]
    positions = [(-200, 100), (0, 100), (200, 100), (-100, -100), (100, -100)]
    
    for pos, angle in zip(positions, angles):
        t.penup()
        t.goto(pos)
        t.pendown()
        draw_cluster(t, size, angle)
    
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()