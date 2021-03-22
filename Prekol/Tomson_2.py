import matplotlib.pyplot as plt
import numpy as np
x_2 = [3.9, 3.5, 3.0, 2.5, 2.0, 1.5, 1]
y_2 = [2.79, 2.43, 2.2, 1.68, 1.27, 1.10, 0.79]
plt.errorbar(x_2, y_2, xerr=0.1, yerr=0.07, ls='none')
plt.grid()
plt.xlabel('Перепад давления, Бар') # подпись осей
plt.ylabel('Перевад температуры, K')
plt.title(r"Зависимость перепада температуры от перепада давления при температуре $35^{\circ}$C") # подпись графика
plt.xlim(0.5, 4)
plt.ylim(0.5, 3)
x = np.arange(0.5, 4.001, 0.001)
plt.plot(x * 1.4 + 0, x)
plt.show()