import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-100, 100.01, 0.01) # создание массива значений
plt.figure(figsize=(28, 8)) # размеры окна графика
n = int(input())
a = float(input())
b = float(input())

plt.xlabel(r'$x$') # подпись осей
plt.ylabel(r'$f(x)$')
plt.title(r'Функция Вейейрштрасса') # подпись графика
plt.grid(True) # сетка
# savefig("figure_with_legend.png") # сохранения графика
plt.show() # вывод графического окна
# fonsize - разные шрифты
