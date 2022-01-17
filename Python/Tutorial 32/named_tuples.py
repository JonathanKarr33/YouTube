from collections import namedtuple
color = namedtuple("color",("red","green","blue"))
first_color = color(123,87,54)
second_color = color(red = 234, blue = 54, green = 22)
print(first_color[0])
print(first_color)
print(first_color.blue)
print(second_color)