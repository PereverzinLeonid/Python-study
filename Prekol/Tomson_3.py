import matplotlib.pyplot as plt
import numpy as np
x_3 = [3.9, 3.5, 3.0, 2.5, 2.0, 1.5, 1]
y_3 = [2.79, 2.77, 2.17, 1.85, 1.62, 1.50, 1.52]
plt.errorbar(x_3, y_3, xerr=0.1, yerr=0.07, ls='none')
plt.grid()
plt.xlabel('Перепад давления, Бар') # подпись осей
plt.ylabel('Перевад температуры, K')
plt.title(r"Зависимость перепада температуры от перепада давления при температуре $50^{\circ}$C") # подпись графика
plt.xlim(0.5, 4)
plt.xlim(0.5, 4)
plt.ylim(1, 3)
x = np.arange(0.5, 4.001, 0.001)
plt.plot(x * 1.7 - 1.0, x)
plt.show()