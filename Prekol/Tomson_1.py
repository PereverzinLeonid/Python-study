import matplotlib.pyplot as plt
import numpy as np
x_1 = [3.9, 3.5, 3.0, 2.5, 2.0, 1.5, 1]
y_1 = [2.80, 2.41, 1.89, 1.52, 0.98, 0.54, 0.05]
plt.errorbar(x_1, y_1, xerr=0.1, yerr=0.07, ls='none')
plt.grid()
plt.xlabel('Перепад давления, Бар') # подпись осей
plt.ylabel('Перевад температуры, K')
plt.title(r"Зависимость перепада температуры от перепада давления при температуре $22^{\circ}$C") # подпись графика
plt.xlim(0.5, 4)
plt.ylim(-0.5, 3)
x = np.arange(-0.5, 4.001, 0.001)
plt.plot(x * 1.03 + 1, x)
plt.show()