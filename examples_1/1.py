# Найти площадь и периметр прямоугольного треугольника по двум заданным катетам.

import math

# ab = input('Введите длину первого катета: ')
# ac = input('Введите длину второго катета: ')

# ab = float(ab)
# ac = float(ac)

# bc = math.sqrt(ab ** 2 + ac ** 2)

# s = (ab * ac) / 2
# p = ab + ac + bc

# print('Площадь треуголника: ', s)
# print('Периметр треугольника: ', p)


def s(x, y):
    print ('Площадь треугольника = ', (x * y) / 2)


def p(x, y):
    res = (math.sqrt(x ** 2 + y ** 2))
    sum = res + x + y
    print('Периметр треугольника = '"%.2f" % sum)


s(5, 1)
p(5, 1)