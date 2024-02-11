from turtle import Turtle, Screen
import random

def rand_rgb():
  rand_int_list = []
  for _ in range(3):
    rand_int_list.append(random.uniform(0, 1))
  return tuple(rand_int_list)

t = Turtle()
t.speed(0)
size_of_gap = 6
num_circle = 360 // size_of_gap

for i in range(num_circle):
  t.pencolor(rand_rgb())
  t.circle(100)
  t.left(size_of_gap)

s = Screen()
s.exitonclick()