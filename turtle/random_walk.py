from turtle import Turtle, Screen
import random

def rand_rgb():
  rand_int_list = []
  for _ in range(3):
    rand_int_list.append(random.uniform(0, 1))
  return tuple(rand_int_list)

def rand_direction():
  direction_list = [t.forward(30), t.backward(30), t.left(90), t.right(90)]
  return random.choice(direction_list)

t = Turtle()
t.pensize(15)
pos_x, pos_y = t.pos()

s = Screen()
border_x, border_y = s.screensize()

print(s.screensize())
print(pos_x, pos_y)


s.exitonclick()