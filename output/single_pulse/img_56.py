import turtle

def draw_pentagon(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(72)

def draw_flower_of_pentagons():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.color("black")
    t.speed(0)  # Fastest drawing speed
    t.penup()
    
    # Central point
    central_x, central_y = 0, 0
    t.goto(central_x, central_y)
    
    # Number of pentagons
    num_pentagons = 8
    angle_between_pentagons = 360 / num_pentagons
    size = 100  # Size of each pentagon
    
    for i in range(num_pentagons):
        t.goto(central_x, central_y)
        t.setheading(i * angle_between_pentagons)
        t.pendown()
        draw_pentagon(t, size)
        t.penup()
    
    t.hideturtle()
    screen.mainloop()

draw_flower_of_pentagons()