from turtle import Turtle, Screen
import random

def rand_rgb():
  rand_int_list = []
  for _ in range(3):
    rand_int_list.append(random.uniform(0, 1))
  return tuple(rand_int_list)

def rand_direction():
  direction_list = ['forward', 'backward', 'left', 'right']
  return random.choice(direction_list)

t = Turtle()
t.pensize(15)
pos_x, pos_y = t.pos()

s = Screen()
border_x, border_y = s.screensize()

while pos_x < border_x or pos_y < border_y or pos_x > -border_x or pos_y > -border_y:
  t.pencolor(rand_rgb())
  direction = rand_direction()
  if direction == 'left':
    t.left(90)
    t.forward(30)
  elif direction == 'right':
    t.right(90)
    t.forward(30)
  elif direction == 'forward':
    t.forward(30)
  else:
    t.backward(30)

s.exitonclick()