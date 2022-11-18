# f(x) = -12x^4*sin(cos(x))-18x^3+5x^2+10x-30
# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0

import numpy as np
from sympy import *
from scipy.optimize import fsolve
from sympy.plotting import plot
init_printing()
interval = np.arange(-30,30) 
x = Symbol('x')
function_x = sympify('-12*x^4*sin(cos(x)) - 18*x^3 + 5*x^2 + 10*x - 30')
left_point = float(input('Задайте начало отрезка: '))
right_point = float(input('Задайте конец отрезка: '))
def f(x):
    return - 12 * x ** 4 * np.sin(np.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30
number = left_point
roots = []
growth_interval = []
while number < right_point:
    if f(number) >= 0 and f(number + 1) <= 0:
        w = fsolve(f, number)
        roots.append(*w)
    if f(number) <= 0 and f(number + 1) >= 0:
        w = fsolve(f, number)
        roots.append(*w)
    if f(number) > f(number + 1) < f(number + 2):
        growth_interval.append(number + 1)
    number += 1
print(f'Roots: {roots}')
def search_top(left, right):
    array = []
    temp = left
    sum_y = 0
    while left < right:
        array.append([f(left), left])
        left += 0.1
        sum_y += f(left)
    if sum_y > 0:
        sum_y = 0
        print(f'f > 0 {temp, right}')
        return max(array)
    else:
        sum_y = 0
        print(f'f < 0 {temp, right}')
        return min(array)
if len(roots) < 2:
    print('Нет вершин')
else:
    top = []
    for i in range(len(roots) - 1):
        top.append(search_top(roots[i], roots[i + 1]))
    [print(f'Координаты вершин: ({item[1]}, {item[0]})') for item in top]
    if len(top) < 2:
        print('не достаточно данных')
    else:
        for i in range(len(top) - 1):
            if top[i][0] > top[i + 1][0]:
                print(f'Убывает при x {top[i][1], top[i + 1][1]}')
            else:
                print(f'Возрастает при x {top[i][1], top[i + 1][1]}')
plot(function_x)
  