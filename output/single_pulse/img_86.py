import turtle
import math

def draw_heptagon(t, size):
    for _ in range(7):
        t.forward(size)
        t.left(360 / 7)

def move_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.color("black")
    t.speed(0)

    # Heptagon size
    size = 100

    # Calculate the height of the heptagon
    heptagon_height = size * (1 + math.cos(math.radians(360 / 7)) / 2)

    # Calculate the distance between the centers of the heptagons
    # to form an equilateral triangle
    distance = heptagon_height * 2

    # Bottom center heptagon
    move_to(t, 0, -distance / 2)
    draw_heptagon(t, size)

    # Top left heptagon
    move_to(t, -distance / 2, distance / 2)
    draw_heptagon(t, size)

    # Top right heptagon
    move_to(t, distance / 2, distance / 2)
    draw_heptagon(t, size)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()