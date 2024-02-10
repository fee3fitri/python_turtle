from turtle import Turtle, Screen
import random

def rand_rgb():
  rand_int_list = []
  for _ in range(3):
    rand_int_list.append(random.uniform(0, 1))
  return tuple(rand_int_list)

def rand_direction():
  direction_list = [0, 90, 180, 270]
  return random.choice(direction_list)

t = Turtle()
t.pensize(15)
t.speed(0)
pos_x, pos_y = t.pos()

s = Screen()
border_x, border_y = s.screensize()

while pos_x < border_x or pos_y < border_y or pos_x > -border_x or pos_y > -border_y:
  t.pencolor(rand_rgb())
  direction = rand_direction()
  t.forward(30)
  t.setheading(direction)

s.exitonclick()