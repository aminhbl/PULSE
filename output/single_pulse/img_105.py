import turtle

def draw_semicircle(t, radius, direction):
    t.setheading(direction)
    t.circle(radius, 180)

def draw_cluster(t, large_radius, small_radius, direction):
    draw_semicircle(t, large_radius, direction)
    t.penup()
    t.forward(large_radius + small_radius)
    t.pendown()
    draw_semicircle(t, small_radius, direction + 180)
    t.penup()
    t.backward(large_radius + small_radius)
    t.pendown()

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.color("black")
    t.pensize(2)
    t.speed(0)
    
    large_radius = 100
    small_radius = 50
    angle_between_clusters = 360 / 3
    
    for i in range(3):
        draw_cluster(t, large_radius, small_radius, 90)
        t.penup()
        t.goto(0, 0)
        t.setheading(angle_between_clusters * (i + 1))
        t.pendown()
    
    t.hideturtle()
    screen.mainloop()

main()