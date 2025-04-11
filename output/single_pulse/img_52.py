import turtle

def draw_pentagon(t, side_length):
    for _ in range(5):
        t.forward(side_length)
        t.right(72)

def draw_three_pentagons():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.color("black")
    t.speed(0)
    
    side_length = 100
    
    # Draw the first pentagon
    t.penup()
    t.goto(0, 0)
    t.pendown()
    draw_pentagon(t, side_length)
    
    # Draw the second pentagon
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.right(72)
    draw_pentagon(t, side_length)
    
    # Draw the third pentagon
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.right(72)
    draw_pentagon(t, side_length)
    
    t.hideturtle()
    screen.mainloop()

draw_three_pentagons()