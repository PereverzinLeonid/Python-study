import matplotlib.pyplot as plt
import numpy as np
x = [21.3, 25.1, 30.1, 35.1, 40.1, 45.1, 50.1, 55.1, 60.4]
y = [3.7914, 4.4678, 5.3578, 6.2478, 7.1377999999999995, 8.0278, 8.9178, 9.8078, 10.751199999999999]
plt.errorbar(x, y, xerr=0.1, yerr=0.734, ls='none')
plt.grid()
plt.xlabel('Tемпература, K') # подпись осей
plt.ylabel('Теплота образования еденицы поверхности жидкости, Дж/м^2')
plt.title("Зависимость теплоты образования единицы поверхности жидкости от температуры") # подпись графика
p, v = np.polyfit(x, y, deg=1, cov=True)
p_f = np.poly1d(p)
a = p_f(20)
b = p_f(60)
x = np.arange(15, 67.01, 0.01)
plt.plot(x, x * (0.178))
plt.show()