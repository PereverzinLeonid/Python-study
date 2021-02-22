import numpy as np # r говорит о наличии спецсимволов
import matplotlib.pyplot as plt

x = np.arange(-10, 10.01, 0.01) # создание массива значений
plt.figure(figsize=(30, 7)) # размеры окна графика
plt.plot(x, np.sin(x), label=r'$f_1(x)=\sin(x)$')
plt.plot(x, np.cos(x), label=r'$f_2(x)=\cos(x)$')
plt.plot(x, -x, label=r'$f_3(x)=-x$') # построение графика
plt.xlabel(r'$x$') # подпись осей
plt.ylabel(r'$f(x)$')
plt.title(r'$f_1(x)=\sin(x),\ f_2(x)=\cos(x),\ f_3(x)=-x$') # подпись графика
plt.grid(True) # сетка
plt.legend(loc='best', fontsize=14) # легенда
# savefig("figure_with_legend.png") # сохранения графика
plt.show() # вывод графического окна
# fonsize - разные шрифты


