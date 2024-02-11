import colorgram
from turtle import Turtle, Screen
import random


def random_color():
    num_color = 100
    colors = colorgram.extract('spot_painting.jpg', num_color)
    rgb_float = random.choice(colors).rgb
    return rgb_float


t = Turtle()
s = Screen()

dot_size = 30
gap = dot_size * 2
dot_num = 15
screen_size = dot_size * 2 * dot_num
width = 400
height = 400
starting_x = -width
starting_y = -height

t.speed(0)
s.colormode(255)
t.penup()
t.hideturtle()
s.screensize(screen_size, screen_size)

for i in range(dot_num):
    t.goto(starting_x, starting_y + gap * i)
    for j in range(dot_num):
        t.pencolor(random_color())
        t.dot(dot_size)
        t.forward(gap)

s.exitonclick()