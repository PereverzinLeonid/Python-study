import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.01, 0.01) # создание массива значений
plt.figure(figsize=(28, 8)) # размеры окна графика
plt.plot(x, x * x - 6 - x)
plt.xlabel(r'$x$') # подпись осей
plt.ylabel(r'$f(x)$')
plt.grid(True) # сетка
plt.show()