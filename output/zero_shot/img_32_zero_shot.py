import turtle

def draw_pentagon(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(72)

def draw_connected_pentagons():
    screen = turtle.Screen()
    screen.setup(width=600, height=400)
    
    t = turtle.Turtle()
    t.pensize(3)
    t.color("black")
    
    # Draw the first pentagon
    t.penup()
    t.goto(-150, 0)
    t.pendown()
    draw_pentagon(t, 100)
    
    # Move to the starting point of the second pentagon
    t.penup()
    t.goto(50, 0)
    t.pendown()
    
    # Draw the second pentagon
    draw_pentagon(t, 100)
    
    # Draw the connecting line
    t.penup()
    t.goto(-50, 0)
    t.pendown()
    t.forward(100)
    
    t.hideturtle()
    screen.mainloop()

draw_connected_pentagons()