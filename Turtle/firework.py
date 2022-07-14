import turtle
from random import random, randint

screen = turtle.Screen()
screen.bgcolor("black")
screen.colormode(255)
t = turtle.Turtle()
t.speed(0)
t.width(3)
t.penup() 

def line_function(turn_degree=10):
    length = randint(1, 150)
    x = randint(-683+2*length, 683-2*length)
    y = randint(-384+2*length, 384-2*length)
    t.goto(x,y)

    for x in range(int(360/turn_degree)+1):
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        t.forward(length)
        t.backward(length)
        t.pendown()
        t.color(red, green, blue)
        t.rt(turn_degree)


for x in range(1, 150) :
    line_function()
    t.penup()

turtle.done()