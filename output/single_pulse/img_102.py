import turtle

def draw_circle(t, radius):
    t.penup()
    t.forward(radius)
    t.left(90)
    t.pendown()
    t.circle(radius)
    t.penup()
    t.right(90)
    t.backward(radius)
    t.pendown()

def draw_semi_circle(t, radius):
    t.penup()
    t.forward(radius)
    t.left(90)
    t.pendown()
    t.circle(radius, 180)
    t.penup()
    t.right(90)
    t.backward(radius)
    t.pendown()

def draw_hexagonal_cluster(t, radius):
    for _ in range(6):
        draw_circle(t, radius)
        t.penup()
        t.forward(2 * radius)
        t.right(60)
        t.pendown()

def draw_surrounding_semi_circles(t, radius):
    t.penup()
    t.forward(2 * radius)
    t.right(90)
    t.pendown()
    for _ in range(6):
        draw_semi_circle(t, radius)
        t.penup()
        t.forward(2 * radius)
        t.right(60)
        t.pendown()

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.color("black")
    
    radius = 20
    
    # Draw the hexagonal cluster of circles
    draw_hexagonal_cluster(t, radius)
    
    # Position for the surrounding semicircles
    t.penup()
    t.goto(0, 0)
    t.pendown()
    
    # Draw the surrounding semicircles
    draw_surrounding_semi_circles(t, radius)
    
    t.hideturtle()
    screen.mainloop()

main()