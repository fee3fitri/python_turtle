from turtle import Turtle, Screen
import random

def rand_rgb():
  rand_int_list = []
  for _ in range(3):
    rand_int_list.append(random.uniform(0, 1))
  return tuple(rand_int_list)

t = Turtle()
colors = []

for i in range (3, 11):
  colors.append(rand_rgb())
  for j in range(i):
    degree = 360 / i
    t.pencolor(colors[i - 3])
    t.right(degree)
    t.forward(100)

screen = Screen()
screen.exitonclick()