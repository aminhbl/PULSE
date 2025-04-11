import turtle

def draw_semi_circle():
    turtle.penup()
    turtle.setheading(90)  # Point upwards
    turtle.pendown()
    turtle.pensize(3)
    turtle.pencolor("black")
    turtle.circle(50, 180)  # Draw a semi-circle
    turtle.penup()

def main():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.bgcolor("white")
    
    # Draw the first semi-circle
    turtle.penup()
    turtle.goto(-150, 0)
    draw_semi_circle()
    
    # Draw the second semi-circle
    turtle.penup()
    turtle.goto(0, 0)
    draw_semi_circle()
    
    # Draw the third semi-circle
    turtle.penup()
    turtle.goto(150, 0)
    draw_semi_circle()
    
    turtle.done()

main()