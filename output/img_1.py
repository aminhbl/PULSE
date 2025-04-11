import turtle
import random

def draw_line(t, length, angle):
    t.setheading(angle)
    t.forward(length)
    t.backward(length)

def draw_complex_image():
    # Setup the turtle environment
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.color("black")
    t.width(2)
    
    # Draw the complex image
    num_lines = 50
    max_length = 200
    for _ in range(num_lines):
        angle = random.uniform(0, 360)
        length = random.uniform(50, max_length)
        draw_line(t, length, angle)
    
    # Hide the turtle and finish
    t.hideturtle()
    screen.mainloop()

draw_complex_image()